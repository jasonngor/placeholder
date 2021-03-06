import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file, liketwitter.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'liketwitter.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('LIKETWITTER_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection for the application if one doesn't already exist
    """
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

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
