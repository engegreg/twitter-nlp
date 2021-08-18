from flask_sqlalchemy import SQLAlchemy
import tweepy
import spacy
import en_core_web_sm
import os


db = SQLAlchemy()


#create user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) #setting id as primary
    name = db.Column(db.String(50), nullable=False) #column for usernames

    #string representation function, allows values to be called and printed.
    def __repr__(self):
        return "<User: {}>".format(self.name)


#creating table for tweets

class tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)