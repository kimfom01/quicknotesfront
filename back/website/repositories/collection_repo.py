from ..models.Collection import Collection
from ..schema.Response import Response
from .. import db


DEFAULT_COLLECTION = "Default Collection"


class CollectionRepo:
    def get_collections(self, user_id: int) -> Response:
        collections = Collection.query.filter_by(user_id=user_id).all()

        if collections is None:
            return Response(success=False, message="Collections not found", body=None)
        return Response(success=True, message="Success", body=collections)

    def get_default_collection(self, user_id: int) -> Response:
        collection = Collection.query.filter_by(
            user_id=user_id, title=DEFAULT_COLLECTION
        ).first()

        if collection is None:
            return Response(
                success=False, message="Default Collection not found", body=None
            )
        return Response(success=True, message="Success", body=collection)

    def create_collection(self, title: str, user_id: int) -> Response:
        try:
            collection = Collection(title=title, user_id=user_id)

            db.session.add(collection)
            db.session.commit()
            db.session.refresh(collection)

            return Response(
                success=True, message="Successfully created", body=collection
            )
        except:
            return Response(success=False, message="Unable to create", body=None)


collection_repo = CollectionRepo()
