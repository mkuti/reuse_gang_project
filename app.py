import os, json
from flask import Flask, render_template, redirect, request, url_for, jsonify, flash, session
from flask_session import Session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from os import path
# import file where username and password of MongoDB is saved
if path.exists("env.py"):
    import env

app = Flask(__name__)  # create instance of flask
sess = Session()  # create session object

# add configuration to Flask app
MONGO_URI = os.environ["MONGODB_URI"]
app.secret_key = os.urandom(24)
SECRET_KEY = os.urandom(24)
sess.init_app(app)
app.config["MONGODB_NAME"] = "reuse-gang"
app.config["MONGO_URI"] = MONGO_URI

# create an instance of Pymongo with app object being pushed as argument
mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('/pages/home.html', items=mongo.db.items.find(),
                           users=mongo.db.users.find(), title="Re-Use Gang")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        users = mongo.db.users
        used_name = users.find_one({'username': request.form["username"]})

        if used_name is None:
            user_pwd = generate_password_hash(request.form["password"])
            users.insert_one({"username": request.form["username"], "password": user_pwd})
            session['username'] = request.form["username"]
            flash("Welcome to the Gang, session['username']!")
            return redirect(url_for('home'))
        else:
            flash("This username already exists, please choose another one")
            return render_template('/components/register.html')

    return render_template('/components/register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('/components/login.html')


@app.route('/items/filter', methods=["POST", "GET"])
def filter_items():
    items = mongo.db.items
    category = request.form["item_category"].capitalize()
    filtered_items = items.find({'item_category': category})
    return render_template('/pages/filtered_items.html', 
                           filtered_items=filtered_items)


@app.route('/items/add', methods=["POST", "GET"])
def add_item():
    if request.method == "POST":
        items = mongo.db.items
        items.insert_one(request.form.to_dict())
        return redirect(url_for('home'))
    return render_template('/pages/additem.html')


@app.route('/items/update/<item_id>', methods=["POST", "GET"])
def update_item(item_id):
    if request.method == "GET":
        clicked_item = mongo.db.items.find_one({'_id': ObjectId(item_id)})
        return render_template('/pages/updateitem.html')
    else:
        clicked_item.update(request.form.to_dict())
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)
