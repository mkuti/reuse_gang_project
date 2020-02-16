import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):  # import file where username and password of MongoDB is saved
    import env

app = Flask(__name__)  # create instance of flask

# add configuration to Flask app
MONGO_URI = os.environ["MONGODB_URI"]
SECRET_KEY = os.environ["SECRET_KEY"]
app.config["MONGODB_NAME"] = "reuse-gang"
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)  # create an instance of Pymongo with app object being pushed as argument

@app.route('/')
@app.route('/home')
def home():
    return render_template('/pages/home.html', items=mongo.db.items.find(), users=mongo.db.users.find())

@app.route('/login')
def login():
    return render_template('/components/login.html')

@app.route('/register')
def register():
    return render_template('/components/register.html')


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")), 
            debug=True)
