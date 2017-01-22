import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from amazon.api import AmazonAPI
from random import randint
import json
import os

# os.chdir("..") # change to file path
# os.chdir("..")
#
# f = open("pswd.txt", "r")
# st = f.read(200).strip("\n").split(" ")
#
# AMAZON_ACCESS_KEY = st[0]
# AMAZON_SECRET_KEY = st[1]
# AMAZON_ASSOC_TAG  = st[2]
#
# amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
# product = amazon.lookup(ItemId='B00EOE0WKQ')
# print(product.title)

app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file, liketwitter.py
#amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

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

@app.route("/product_page")
def initAmazon():
    os.chdir("..") # change to file path
    os.chdir("..") # change to file path
    os.chdir("..") # change to file path
    f = open("pswd.txt", "r")
    st = f.read(200).strip("\n").split(" ")
    os.chdir("placeholder")
    os.chdir("AmazonRoulette")
    os.chdir("AmazonRoulette")

    AMAZON_ACCESS_KEY = st[0]
    AMAZON_SECRET_KEY = st[1]
    AMAZON_ASSOC_TAG  = st[2]

    amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
    return redirect("www.amazon.com/dp/B00014D6QU")

# @app.route("/get-product", methods=[GET])
# def getRandomProduct():
#     found = False
#     product = None
#     while not found:
#         asin = ""
#         letterstring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         for _ in range(10):
#             randomnum = randint(0,35)
#             if (randomnum <= 9):
#                 asin += str(randomnum)
#             else:
#                 asin += letterstring[randomnum - 10]
#         try:
#             product = amazon.lookup(asin)
#             found = True
#         except Exception:
#             found = False
#     return json.dump(product)
    return amazon

@app.route('/')
    def home():
        """Takes user to index.html"""
        return render_template("index.html")
def getSpecificProduct():
    pass

@app.route("/get-product", methods=[GET])
def getRandomProduct():
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



@app.route('/searchPage')
    def signup():
        """Takes user to signup.html"""
        return render_template("signup.html")
