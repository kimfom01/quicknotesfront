from typing import List
from ..models.Collection import Collection
from ..models.Note import Note
from ..schema.Response import Response
from .. import db


class NotesRepo:
    def get_by_id(self, id: int, collection_id: int) -> Note:
        return Note.query.filter_by(collection_id=collection_id, id=id).first()

    def get_all(self, collection_id: int) -> List[Note]:
        return Note.query.filter_by(collection_id=collection_id, deleted=False).all()

    def get_collections(self, user_id: int) -> List[Collection]:
        return Collection.query.filter_by(user_id=user_id).all()

    def create_note(self, data: str, user_id: int, collection_id: int) -> Note:
        note = Note(
            data=data, user_id=user_id, collection_id=collection_id, deleted=False
        )

        db.session.add(note)
        db.session.commit()
        db.session.refresh(note)

        return note

    def delete_note(self, note_id: int, collection_id: int) -> None:
        note = Note.query.filter_by(id=note_id, collection_id=collection_id).first()

        if note is None:
            return Response(success=False, message="Note not found", body=None)

        try:
            note.deleted = True
            db.session.commit()
        except:
            raise Exception("Unable to delete")


notes_repo = NotesRepo()
