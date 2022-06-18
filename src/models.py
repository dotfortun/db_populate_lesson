from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    username = db.Column(db.String(120), unique=False, nullable=True)
    password = db.Column(db.String(120), unique=False, nullable=True)
    title = db.Column(db.String(120), unique=False, nullable=True)
    first_name = db.Column(db.String(120), unique=False, nullable=True)
    last_name = db.Column(db.String(120), unique=False, nullable=True)
    phone = db.Column(db.String(120), unique=False, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, onupdate=datetime.now, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(120), unique=False, nullable=True)
    phonetic = db.Column(db.String(120), unique=False, nullable=True)
    mandarin = db.Column(db.String(120), unique=False, nullable=True)
    phoneticM = db.Column(db.String(120), unique=False, nullable=True)
    images = db.Column(db.String(120), unique=False, nullable=True)
    part_of_speech = db.Column(db.String(120), unique=False, nullable=True)
