from ..models.Collection import Collection
from ..models.Note import Note
from ..schema.Response import Response
from .. import db


class NotesRepo:
    def get_by_id(self, id: int, collection_id: int) -> Response:
        note = Note.query.filter_by(collection_id=collection_id, id=id).first()

        if note is None:
            return Response(success=False, message="Note not found", body=None)
        return Response(success=True, message="Success", body=note)

    def get_all(self, collection_id: int) -> Response:
        notes = Note.query.filter_by(collection_id=collection_id).all()

        if notes is None:
            return Response(success=False, message="Notes not found", body=None)
        return Response(success=True, message="Success", body=notes)

    def get_collections(self, user_id: int) -> Response:
        collections = Collection.query.filter_by(user_id=user_id).all()

        if collections is None:
            return Response(success=False, message="Collections not found", body=None)
        return Response(success=True, message="Success", body=collections)

    def create_note(self, data: str, user_id: int, collection_id: int) -> Response:
        try:
            note = Note(data=data, user_id=user_id, collection_id=collection_id)

            db.session.add(note)
            db.session.commit()
            db.session.refresh(note)

            return Response(success=True, message="Successfully created", body=note)
        except:
            return Response(success=False, message="Unable to create", body=None)

    def delete_note(self, note_id: int, collection_id: int) -> Response:
        note = Note.query.filter_by(id=note_id, collection_id=collection_id).first()

        if note is None:
            return Response(success=False, message="Note not found", body=None)

        try:
            db.session.delete(note)
            db.session.commit()

            return Response(success=True, message="Successfully deleted", body=None)
        except:
            return Response(success=False, message="Unable to delete", body=None)


notes_repo = NotesRepo()
