import json
from flask import Blueprint, request, render_template, jsonify, flash
from flask_login import login_required, current_user
from .models import Note, Collection
from . import db


notes = Blueprint("notes", __name__)


@notes.route("my-notes", methods=["GET"])
@login_required
def my_notes():
    """
    Show list of notes
    """

    collection_id = request.args.get("collection_id")

    collection = Collection.query.get(collection_id)

    return render_template("my_notes.html", user=current_user, collection=collection)


@notes.route("/my-collections", methods=["GET"])
@login_required
def my_collections():
    """
    Show collections
    """
    collection_id = request.args.get("collection_id")

    collection = Collection.query.get(collection_id)

    return render_template(
        "my_collections.html", user=current_user, collection=collection
    )


@notes.route("/new-note", methods=["GET", "POST"])
@login_required
def new_note():
    """
    Create new note
    """
    collection_id = Collection.query.filter_by(user_id=current_user.id).first().id
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short", category="error")
        else:
            created_note = Note(
                data=note, user_id=current_user.id, collection_id=collection_id
            )

            db.session.add(created_note)
            db.session.commit()
            flash("Note saved!", category="success")
    return render_template("new_note.html", user=current_user)


@notes.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    """
    Delete existing note api endpoint
    """
    data = json.loads(request.data)
    note_id = data["noteId"]

    note = Note.query.get(note_id)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
