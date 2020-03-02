import os
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

# add configuration to Flask app
app.secret_key = os.getenv("SECRET_KEY")
app.config["MONGODB_NAME"] = "reuse-gang"
app.config["MONGO_URI"] = os.environ["MONGODB_URI"]

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
        used_email = users.find_one({'email': request.form["email"]})

        if used_name and used_email is None:
            user_pwd = generate_password_hash(request.form["password"])
            users.insert_one({
                "username": request.form["username"],
                "email": request.form["email"], 
                "password": user_pwd
                })
            session['username'] = request.form["username"]
            flash("Welcome to the Gang, session['username']!")
            return redirect(url_for('home'))
        elif used_email is not None:
            flash("This email address is already registered, would you like to log in instead?")
            return redirect(url_for('login'))
        else:
            flash("This username already exists, please choose another one")
            return redirect(url_for('register'))

    return render_template('/components/register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():    
    return render_template('/components/login.html')


@app.route('/items/filter', methods=["POST", "GET"])
def filter_items():
    items = mongo.db.items
    cat = request.get_json().lower()
    print(cat)
    filtered_items = items.find({'item_category': json.dumps(cat)})
    print(filtered_items)
    return render_template('/pages/filtered_items.html', filtered_items=filtered_items)


@app.route('/items/add', methods=["POST", "GET"])
def add_item():
    categories = ["Kids", "Outdoor", "Household", "Other"]
    if request.method == "POST":
        items = mongo.db.items
        items.insert_one(request.form.to_dict())
        flash("Thanks!Your free stuff will be shared immediately with the gang.")
        return redirect(url_for('home'))
    return render_template('/pages/additem.html', categories=categories)


@app.route('/items/update/<item_id>', methods=["POST", "GET"])
def update_item(item_id):
    #if method to call function is POST which post data from front-end to back-end, we update database with form result and redirect user to home
    if request.method == "POST":
        items = mongo.db.items
        items.update({'_id': ObjectId(item_id)},
                     {
            'item_name': request.form.get('item_name'),
            'item_category': request.form.get('item_category'),
            'item_description': request.form.get('item_description'),
            'item_img': request.form.get('item_img')
            })
        return redirect(url_for('home'))
    # if the method to call function is GET which is default, we find item matching clicked item on any card and return template where user can edit item
    else:
        clicked_item = mongo.db.items.find_one({'_id': ObjectId(item_id)})
        return render_template('/pages/updateitem.html', item=clicked_item)     


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)
