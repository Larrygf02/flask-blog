# coding: utf-8
from sqlalchemy import ARRAY, Column, DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Draft(db.Model):
    __tablename__ = 'drafts'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime(True))
    updated_at = db.Column(db.DateTime(True))
    deleted_at = db.Column(db.DateTime(True), index=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey('users.id'))

    user = db.relationship('User', primaryjoin='Draft.user_id == User.id', backref='drafts')



class StorieApplaus(db.Model):
    __tablename__ = 'storie_applauses'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime(True))
    updated_at = db.Column(db.DateTime(True))
    deleted_at = db.Column(db.DateTime(True), index=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    storie_id = db.Column(db.ForeignKey('stories.id'), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    storie = db.relationship('Story', primaryjoin='StorieApplaus.storie_id == Story.id', backref='storie_applauses')
    user = db.relationship('User', primaryjoin='StorieApplaus.user_id == User.id', backref='storie_applauses')



class StorieComment(db.Model):
    __tablename__ = 'storie_comments'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'storie_id'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime(True))
    updated_at = db.Column(db.DateTime(True))
    deleted_at = db.Column(db.DateTime(True), index=True)
    user_id = db.Column(db.Integer)
    storie_id = db.Column(db.Integer)
    content = db.Column(db.Text)



class StorieVisit(db.Model):
    __tablename__ = 'storie_visits'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime(True))
    updated_at = db.Column(db.DateTime(True))
    deleted_at = db.Column(db.DateTime(True), index=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    storie_id = db.Column(db.ForeignKey('stories.id'), nullable=False)

    storie = db.relationship('Story', primaryjoin='StorieVisit.storie_id == Story.id', backref='storie_visits')
    user = db.relationship('User', primaryjoin='StorieVisit.user_id == User.id', backref='storie_visits')



class Story(db.Model):
    __tablename__ = 'stories'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime(True))
    updated_at = db.Column(db.DateTime(True))
    deleted_at = db.Column(db.DateTime(True), index=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey('users.id'))
    user_refer = db.Column(db.Integer)

    user = db.relationship('User', primaryjoin='Story.user_id == User.id', backref='stories')



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime(True))
    updated_at = db.Column(db.DateTime(True))
    deleted_at = db.Column(db.DateTime(True), index=True)
    nickname = db.Column(db.String(70), nullable=False, unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    favorites = db.Column(db.ARRAY(Integer()))
    archiveds = db.Column(db.ARRAY(Integer()))
