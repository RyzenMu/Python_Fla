 
from flask import Blueprint , render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db 
import json

views = Blueprint('views', __name__)

# @views.route("/")
# def home():
#     return "<h1>TEST</h1>"

@views.route("/", methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user, variable1="This is variable 1", user1="muruga")


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = data['note']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({{}})

