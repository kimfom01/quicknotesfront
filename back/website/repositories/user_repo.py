from ..models.User import User
from ..schema.Response import Response
from werkzeug.security import generate_password_hash
from .. import db


class UserRepo:
    def get_by_email(self, email: str) -> Response:
        user = User.query.filter_by(email=email).first()

        if user is None:
            return Response(success=False, message="User not found", body=None)
        return Response(success=True, message="Success", body=user)

    def create_user(self, email: str, first_name: str, password: str) -> Response:
        try:
            password_hash = generate_password_hash(password, method="sha256")
            user = User(email=email, first_name=first_name, password=password_hash)

            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)

            return Response(success=True, message="Successfully created", body=user)
        except:
            return Response(success=False, message="Unable to create", body=None)


user_repo = UserRepo()
