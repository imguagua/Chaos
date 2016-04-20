from datetime import datetime
from flask import current_app
from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.name


class Entity(db.Model):
    __tablename__ = 'entitys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    create_since = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Entity %r>' % self.name


class Scene(db.Model):
    __tablename__ = 'scenes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(64))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    create_since = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Scene %r>' % self.name
