from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db


class User(db.Model, UserMixin):
    """
    User model definition
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    collections = db.relationship("Collection", backref="User", passive_deletes=True)
    notes = db.relationship("Note", backref="User", passive_deletes=True)


class Collection(db.Model):
    """
    Collection model definition
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))
    notes = db.relationship("Note", backref="Collection", passive_deletes=True)


class Note(db.Model):
    """
    Note model definition
    """

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))
    collection_id = db.Column(db.Integer, db.ForeignKey("collection.id"))
