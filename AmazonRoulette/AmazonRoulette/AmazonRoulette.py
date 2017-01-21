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
