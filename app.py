from flask import Flask
from flask import request
from flask import render_template
from .models import db, tweet, User
import tweepy
import os

#API keys

TWITTER_API_KEY = "0sQenxDnWlWzWDaPp4wXIezZP"
TWITTER_API_SECRET = "jFwr48Bn61Z0od59CzY1SGCypSJxRMgVLX3fMy8aNkoAXkjf7X"

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)

twitter = tweepy.API(auth)

def create_app():

    app_dir = os.path.dirname(os.path.abspath(__file__))
    database = "sqlite:///{}".format(os.path.join(app_dir, "twitoff.sqlite3"))
    app = Flask(__name__)


    #create db
    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    # Create tables
    with app.app_context():
        db.create_all()

    @app.route("/", methods=["GET", "POST"])
    def home():
        name = request.form.get("name")

        if name:
            user = User(name='name')
            db.session.add(user)
            db.session.commit()
        tweet = request.form.get("text")

        if tweet:
            tweet = Tweet(text=text)
            db.session.add(user)
            db.session.add(tweet)
            db.session.commit()
        
            
        return render_template("home.html", user=users)

