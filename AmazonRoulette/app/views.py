from app import app
from flask import render_template, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template("/index.html")

@app.route('/searchpage')
def searchpage():
    return render_template("/searchpage.html")

@app.route('/product_page')
def product_page():
    return redirect("http://www.amazon.com/dp/B00014D6QU")
