from os import getenv
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

from .. import oauth
from ..models.User import User
from ..repositories.user_repo import user_repo
from ..repositories.collection_repo import collection_repo

auth = Blueprint("auth", __name__)
DEFAULT_COLLECTION = "Default Collection"

load_dotenv()


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    Login user with form
    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(password) < 7:
            flash("Password must be greater than 6 characters", category="error")
        else:
            response = user_repo.get_by_email(email=email)

            if not response.success:
                flash("User does not exist!", category="error")

                return render_template("login.html", user=current_user)

            user = response.body

            response = collection_repo.get_default_collection(user_id=user.id)

            if not response.success:
                flash(response.message, category="error")
                return

            default_collection = response.body

            if not user.password:
                flash("You do not have a password!", category="error")
                flash("Click Sign in with Google to continue", category="error")

                return render_template("login.html", user=current_user)

            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)

                return redirect(
                    url_for("notes.my_notes", collection_id=default_collection.id)
                )

            flash("Invalid email or password!", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/demo-login", methods=["GET"])
def demo_login():
    """
    Demo login for guests and explorers
    """

    email = getenv("DEMO_USERNAME")

    response = user_repo.get_by_email(email=email)

    if not response.success:
        flash(
            "Something is wrong. Try to again or create your account to login",
            category="error",
        )
        return render_template("login.html", user=current_user)

    user = response.body

    flash("Logged in successfully!", category="success")
    login_user(user, remember=False)
    return redirect(url_for("notes.my_collections"))


@auth.route("/logout")
@login_required
def logout():
    """
    Logs the user out of the application.
    Clears user session
    """
    session.clear()
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    """
    Sign up with form
    """
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        response = user_repo.get_by_email(email=email)

        if response.success:
            flash("User already exist!", category="error")

            return render_template("sign_up.html", user=current_user)

        if len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif len(password1) < 7:
            flash("Password must be greater than 6 characters", category="error")
        elif password1 != password2:
            flash("Password and Confirm Password must match", category="error")
        else:
            password_hash = generate_password_hash(password1, method="sha256")
            new_user = User(email=email, first_name=first_name, password=password_hash)
            response = user_repo.create_user(new_user)

            if response.success:
                user = response.body

                response = collection_repo.create_collection(
                    title=DEFAULT_COLLECTION, user_id=user.id
                )

                if not response.success:
                    flash("Account created but no default category", category="warning")
                else:
                    flash("Account created!", category="success")

                login_user(user)

                return redirect(url_for("notes.my_notes"))

    return render_template("sign_up.html", user=current_user)


@auth.route("/google-signin")
def google_signin():
    """
    Redirect to google sso

    Return: redirects to callback function
    """
    return oauth.notes_app.authorize_redirect(
        url_for("auth.callback_url", _external=True)
    )


@auth.route("/authCallback")
def callback_url():
    """sumary_line
    Gets the token from google oauth and log in the
    user or create a new user if user doesn't have an account

    Return: redirects to the user's notes
    """
    token = oauth.notes_app.authorize_access_token()
    session["user"] = token
    user_info = session["user"].get("userinfo")
    email = user_info.get("email")

    response = user_repo.get_by_email(email=email)

    if response.success:
        user = response.body
        login_user(user)
        flash("Logged in successfully!", category="success")

        response = collection_repo.get_default_collection(user_id=user.id)

        if not response.success:
            flash(response.message, category="error")
            return

        default_collection = response.body

        return redirect(url_for("notes.my_notes", collection_id=default_collection.id))

    google_user = User(first_name=user_info.get("given_name"), email=email)
    response = user_repo.create_user(google_user)

    if response.success:
        response = collection_repo.create_collection(
            title=DEFAULT_COLLECTION, user_id=google_user.id
        )

        if not response.success:
            flash("Account created but no default category", category="warning")
        else:
            flash("Account created!", category="success")
        login_user(google_user)
        return redirect(url_for("notes.my_notes"))

    flash("Something wen't wrong during google login", category="error")
    return redirect(url_for("auth.login"))
