import os, json
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from os import path
# import file where username and password of MongoDB is saved
if path.exists("env.py"):
    import env

app = Flask(__name__)  # create instance of flask

# add configuration to Flask app
MONGO_URI = os.environ["MONGODB_URI"]
SECRET_KEY = os.environ["SECRET_KEY"]
app.config["MONGODB_NAME"] = "reuse-gang"
app.config["MONGO_URI"] = MONGO_URI

# create an instance of Pymongo with app object being pushed as argument
mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('/pages/home.html', items=mongo.db.items.find(),
                           users=mongo.db.users.find())


@app.route('/login')
def login():
    return render_template('/components/login.html')


@app.route('/register')
def register():
    return render_template('/components/register.html')


@app.route('/add_item')
def add_item():
    return render_template('/pages/add_item.html')


@app.route('/create_item', methods=["POST"])
def create_item():
    items = mongo.db.items
    items.insert_one(request.form.to_dict())
    return render_template('/pages/home.html')


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)
