"flask 101"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we analyze"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    """Tweets we pull"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280)) 

#applationi

app = Flask(__name__)

#route
@app.route("/")

#function
def create_app():
    app = Flask(__name__)

    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    #have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!!'
    return app


if __name__ == "__main__":
  app.run()