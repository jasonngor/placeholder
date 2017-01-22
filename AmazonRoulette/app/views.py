from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    return render_template("/index.html")

@app.route('/searchpage')
def searchpage():
    return render_template("/searchpage.html")
