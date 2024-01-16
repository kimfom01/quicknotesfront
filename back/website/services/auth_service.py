from website.services.user_service import UserService, user_service
from website.repositories.collection_repo import CollectionRepo, collection_repo
from website.schema.Response import Response
from flask_login import login_user
from werkzeug.security import check_password_hash


class AuthService:
    def __init__(
        self, collection_repo: CollectionRepo, user_service: UserService
    ) -> None:
        self.collection_repo = collection_repo
        self.user_service = user_service

    def login_user(self, email: str, password: str) -> Response:
        if len(password) < 7:
            return Response(
                success=False,
                message="Password must be greater than 6 characters",
                body=None,
            )
        else:
            response = self.user_service.get_by_email(email=email)

            if not response.success:
                return Response(success=False, message=response.message, body=None)

            user = response.body

            response = self.collection_repo.get_default_collection(user_id=user.id)

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

    def sign_up_user():
        pass


auth_service = AuthService(collection_repo, user_service)
