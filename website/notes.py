import json
from flask import Blueprint, request, redirect, url_for, render_template, jsonify, flash
from flask_login import login_required, current_user
from .models import Note, Collection
from . import db


notes = Blueprint("notes", __name__)


@notes.route("my-notes", methods=["GET", "POST"])
@login_required
def my_notes():
    collection_id = request.args.get("collection_id")

    collection = Collection.query.get(collection_id)
    if request.method == "POST":
        return redirect(url_for('views.new_note'))
    return render_template("my_notes.html", user=current_user, collection=collection)


@notes.route("/my-collections", methods=["GET", "POST"])
@login_required
def my_collections():
    collection_id = request.args.get("collection_id")
    print(collection_id)

    collection = Collection.query.get(collection_id)
    print(collection)

    if request.method == "POST":
        return redirect(url_for('views.new_note'))
    return render_template("my_collections.html", user=current_user, collection=collection)


@notes.route("/new-note", methods=["GET", "POST"])
@login_required
def new_note():
    collection_id = Collection.query.filter_by(
        user_id=current_user.id).first().id
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short", category="error")

        else:
            new_note = Note(data=note, user_id=current_user.id,
                            collection_id=collection_id)

            db.session.add(new_note)
            db.session.commit()
            flash("Note saved!", category="success")
    return render_template("new_note.html", user=current_user)


@notes.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    data = json.loads(request.data)
    noteId = data["noteId"]

    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
