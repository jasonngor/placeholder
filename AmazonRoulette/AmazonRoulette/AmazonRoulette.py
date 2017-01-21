import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from werkzeug import generate_password_hash, check_password_hash
from amazon.api import AmazonAPI
from random import randint
import json

app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file, liketwitter.py
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'amazonroulette.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('AMAZONROULETTE_SETTINGS', silent=True)

@app.route("/")
def home():
    return render_template("index.html")

<<<<<<< HEAD
@app.route("/get-product", methods=[GET])
def getproduct():
    found = False
    product = None
    while not found:
        asin = ""
        letterstring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for _ in range(10):
            randomnum = randint(0,35)
            if (randomnum <= 9):
                asin += str(randomnum)
            else:
                asin += letterstring[randomnum - 10]
        try:
            product = amazon.lookup(asin)
            found = True
        except Exception:
            found = False
    return json.dump(product)
=======
# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()
#
# def init_db():
#     db = get_db()
#     with app.open_resource('schema.sql', mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()
#
# @app.cli.command('initdb')
# def initdb_command():
#     """Initializes the database."""
#     init_db()
#     print('Initialized the database.')
#
@app.route('/')
def home():
    """Takes user to index.html"""
    return render_template("index.html")

@app.route('/signup')
def signup():
    """Takes user to signup.html"""
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def adduser():
    db = get_db()
    db.execute("insert into user (username, password) values (?, ?)", [request.form["username"], request.form["password"]])
    db.commit()
    flash("New user added.")
    return redirect(url_for("home"))

@app.route('/login')
def login():
    """Takes user to login.html"""
    return render_template("login.html")
>>>>>>> 6cdc385765987feb5f5939915c23e9e1ba170e8c
