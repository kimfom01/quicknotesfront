from website.schema.Response import Response
from website.services.note_service import NoteService
from website.repositories.notes_repo import NotesRepo
import pytest
from unittest import mock


@pytest.fixture
def note_repo():
    mock_note_repo = mock.create_autospec(NotesRepo)

    yield mock_note_repo


def test_get_by_id_valid(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.get_by_id(id=1, collection_id=1)

    assert response.success == True
    assert response.message == "Success"


def test_get_by_id_collection_id_invalid(note_repo):
    note_repo.get_by_id.return_value = Response(
        success=False,
        message="Id or Collection id cannot be less than or equal to 0",
        body=None,
    )
    note_service = NoteService(note_repo)

    response = note_service.get_by_id(id=1, collection_id=0)

    assert response.success == False
    assert response.message == "Id or Collection id cannot be less than or equal to 0"


def test_get_by_id_note_id_invalid(note_repo):
    note_repo.get_by_id.return_value = Response(
        success=False,
        message="Id or Collection id cannot be less than or equal to 0",
        body=None,
    )
    note_service = NoteService(note_repo)

    response = note_service.get_by_id(id=0, collection_id=1)

    assert response.success == False
    assert response.message == "Id or Collection id cannot be less than or equal to 0"


def test_get_all_valid(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.get_all(collection_id=1)

    assert response.success == True
    assert response.message == "Success"


def test_get_all_invalid(note_repo):
    note_repo.get_all.return_value = Response(
        success=False,
        message="Collection id cannot be less than or equal to 0",
        body=None,
    )
    note_service = NoteService(note_repo)

    response = note_service.get_all(collection_id=0)

    assert response.success == False
    assert response.message == "Collection id cannot be less than or equal to 0"


def test_create_note_valid(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.create_note(data="test data", user_id=1, collection_id=1)

    assert response.success == True
    assert response.message == "Successfully created"


def test_create_note_data_invalid(note_repo):
    note_repo.create_note.return_value = Response(
        success=False, message="Unable to create, data is invalid", body=None
    )
    note_service = NoteService(note_repo)

    response = note_service.create_note(data="", user_id=1, collection_id=1)

    assert response.success == False
    assert response.message == "Unable to create, data is invalid"


def test_create_note_collection_id_invalid(note_repo):
    note_repo.create_note.return_value = Response(
        success=False,
        message="Unable to create, user id or collection id cannot be less than or equal to 0",
        body=None,
    )

    note_service = NoteService(note_repo)

    response = note_service.create_note(data="test data", user_id=1, collection_id=0)

    assert response.success == False
    assert (
        response.message
        == "Unable to create, user id or collection id cannot be less than or equal to 0"
    )


def test_create_note_user_id_invalid(note_repo):
    note_repo.create_note.return_value = Response(
        success=False,
        message="Unable to create, user id or collection id cannot be less than or equal to 0",
        body=None,
    )

    note_service = NoteService(note_repo)

    response = note_service.create_note(data="test data", user_id=0, collection_id=1)

    assert response.success == False
    assert (
        response.message
        == "Unable to create, user id or collection id cannot be less than or equal to 0"
    )


def test_delete_note(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.delete_note(note_id=1, collection_id=1)

    assert response.success == True
    assert response.message == "Successfully deleted"


def test_delete_note_collection_id_invalid(note_repo):
    note_repo.delete_note.side_effect = Exception(
        "Unable to delete, note id or collection id cannot be less than or equal to 0"
    )

    note_service = NoteService(note_repo)

    response = note_service.delete_note(note_id=1, collection_id=0)

    assert response.success == False
    assert (
        response.message
        == "Unable to delete, note id or collection id cannot be less than or equal to 0"
    )


def test_delete_note_note_id_invalid(note_repo):
    note_repo.delete_note.side_effect = Exception(
        "Unable to delete, note id or collection id cannot be less than or equal to 0"
    )

    note_service = NoteService(note_repo)

    response = note_service.delete_note(note_id=0, collection_id=1)

    assert response.success == False
    assert (
        response.message
        == "Unable to delete, note id or collection id cannot be less than or equal to 0"
    )
