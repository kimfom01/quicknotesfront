from website.repositories.user_repo import UserRepo, user_repo
from ..schema.Response import Response
from email_validator import validate_email, EmailNotValidError


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

    def create_user(self, email: str, first_name: str, password: str) -> Response:
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
