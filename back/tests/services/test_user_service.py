from website.services.user_service import UserService
from website.repositories.user_repo import UserRepo
import pytest
from unittest import mock


@pytest.fixture
def user_service():
    mock_user_repo = mock.create_autospec(UserRepo)
    user_service = UserService(mock_user_repo)

    yield user_service


@pytest.fixture
def user_service_invalid():
    mock_user_repo = mock.create_autospec(UserRepo)
    user_service = UserService(mock_user_repo)

    mock_user_repo.get_by_email.return_value = None

    yield user_service


def test_get_by_email_valid(user_service):
    response = user_service.get_by_email(email="demo@mail.com")

    assert response.success == True
    assert response.message == "Success"


def test_get_by_email_invalid(user_service_invalid):
    response = user_service_invalid.get_by_email("janat16@mail.com")

    assert response.success == False
    assert response.message == "User not found"


def test_create_user_valid(user_service):
    response = user_service.create_user(
        email="test@mail.com", first_name="Test", password="Pa$$w0rd"
    )

    assert response.success == True
    assert response.message == "Successfully created"


def test_create_user_invalid(user_service):
    response = user_service.create_user(
        email="testmail.com", first_name="Test", password="Pa$$w0rd"
    )

    assert response.success == False
    assert (
        response.message
        == "The email address is not valid. It must have exactly one @-sign."
    )
