from email_validator import validate_email, EmailNotValidError


from ..repositories.user_repo import UserRepo, user_repo
from ..services.collection_service import CollectionRepo, collection_repo
from ..schema.Response import Response


class UserService:
    def __init__(self, user_repo: UserRepo, collection_repo: CollectionRepo) -> None:
        self.user_repo = user_repo
        self.collection_repo = collection_repo

    def get_by_email(self, email: str) -> Response:
        try:
            emailObject = validate_email(email)

            email = emailObject.normalized

            user = self.user_repo.get_by_email(email=email)

            if user is None:
                return Response(
                    success=False, message="User does not exist!", body=None
                )
            return Response(success=True, message="Success", body=user)
        except EmailNotValidError as errorMsg:
            return Response(success=False, message=str(errorMsg), body=None)

    def create_user(self, email: str, first_name: str, password: str) -> Response:
        try:
            if len(first_name) <= 1:
                raise Exception("First name must be greater than 1 character")
            elif len(password) <= 6:
                raise Exception("Password must be greater than 6 characters")

            emailObject = validate_email(email)

            email = emailObject.normalized

            user = self.user_repo.create_user(
                email=email, first_name=first_name, password=password
            )

            self.collection_repo.create_default_collection(user_id=user.id)
            return Response(success=True, message="Successfully registered", body=user)
        except EmailNotValidError as errorMsg:
            return Response(success=False, message=str(errorMsg), body=None)
        except Exception as ex:
            return Response(success=False, message=str(ex), body=None)


user_service = UserService(user_repo, collection_repo)
