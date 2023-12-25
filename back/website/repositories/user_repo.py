from ..models.User import User
from ..schema.Response import Response
from .. import db


class UserRepo:
    def get_by_email(self, email: str) -> Response:
        user = User.query.filter_by(email=email).first()

        if user is None:
            return Response(success=False, message="User not found", body=None)
        return Response(success=True, message="Success", body=user)

    def create_user(self, user: User) -> Response:
        try:
            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)

            return Response(success=True, message="Successfully created", body=user)
        except:
            return Response(success=False, message="Unable to create", body=None)


user_repo = UserRepo()
