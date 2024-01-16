from flask_login import login_user
from website.repositories.collection_repo import collection_repo
from website.repositories.user_repo import UserRepo, user_repo
from ..schema.Response import Response
from email_validator import validate_email, EmailNotValidError
from werkzeug.security import check_password_hash


class UserService:
    def __init__(self, user_repo: UserRepo) -> None:
        self.user_repo = user_repo

    def get_by_email(self, email: str) -> Response:
        try:
            emailObject = validate_email(email)

            email = emailObject.normalized

            user = self.user_repo.get_by_email(email=email)

            if user is None:
                return Response(success=False, message="User not found", body=None)
            return Response(success=True, message="Success", body=user)
        except EmailNotValidError as errorMsg:
            return Response(success=False, message=str(errorMsg), body=None)

    def login_user(self, email: str, password: str):
        if len(password) < 7:
            return Response(
                success=False,
                message="Password must be greater than 6 characters",
                body=None,
            )
        else:
            response = self.get_by_email(email=email)

            if not response.success:
                return Response(success=False, message=response.message, body=None)

            user = response.body

            response = collection_repo.get_default_collection(user_id=user.id)

            if not response.success:
                return Response(success=False, message=response.message, body=None)

            default_collection = response.body

            if not user.password:
                return Response(
                    success=False,
                    message="You do not have a password!\nClick Sign in with Google to continue",
                    body=None,
                )

            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return Response(
                    success=True,
                    message="Logged in successfully!",
                    body=default_collection,
                )
            return Response(
                success=False,
                message="Invalid email or password!",
                body=None,
            )

    def create_user(self, email: str, first_name: str, password: str) -> Response:
        if len(first_name) <= 1:
            return Response(
                success=False,
                message="First name must be greater than 1 character",
                body=None,
            )
        elif len(password) <= 6:
            return Response(
                success=False,
                message="Password must be greater than 6 characters",
                body=None,
            )
        try:
            emailObject = validate_email(email)

            email = emailObject.normalized

            user = self.user_repo.create_user(
                email=email, first_name=first_name, password=password
            )
            return Response(success=True, message="Successfully created", body=user)
        except EmailNotValidError as errorMsg:
            return Response(success=False, message=str(errorMsg), body=None)
        except:
            return Response(success=False, message="Unable to create", body=None)


user_service = UserService(user_repo)
