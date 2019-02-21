from flask.cli import with_appcontext
import json
import httplib2
from oauth2client.client import FlowExchangeError
from oauth2client.client import flow_from_clientsecrets
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from flask import Flask, render_template, request, redirect,  current_app, g, url_for, flash, jsonify, session as login_session
import random
import string
from datetime import datetime
from databaseSetup import Base, User, Item
from validation import *

app = Flask(__name__)
engine = create_engine('sqlite:///itemCatalog.db')
Base.metadata.bind = engine


with app.app_context():
    g.user = {
        "username":"admin"
    }

DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
 

@app.route('/')
@app.route('/index')
def index():
    items = session.query(Item).all()
    return render_template('index.html', items = items)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        if (checkDuplicateUser(request.form['username'] == False)):
            newUser = User (
                username = request.form['username'],
                pwd = request.form['password']
            )
            session.add(newUser)
            session.commit()
            return redirect(url_for('login'))
        else:
            flash("This username has been used!")
            return render_template('register.html')
    else:
        return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
    for x in xrange(32))
    login_session['state'] = state
    return render_template('signin.html', STATE=state)

@app.route('/logout')
def logout():
    return 'logout'

@app.route('/user/<string:username>/index')
def userIndex(username):
    return 'userIndex'

@app.route('/user/<string:username>/add', methods = ['GET', 'POST'])
def add(username):
    if request.method == 'POST':
        newItem = Item(
            name = request.form['name'],
            description = request.form['description'],
            category = request.form['category'],
            user_id = request.form['user_id']
                    )
        session.add(newItem)
        session.commit()
        return redirect(url_for('userIndex', username = username))
    else :
        return render_template('addItem.html', username = username)

@app.route('/user/<string:username>/<int:itemId>/edit', methods = ['GET', 'POST'])
def edit(username, itemId):
    return 'edit'

@app.route('/user/<string:username>/<int:itemId>/delete', methods = ['GET', 'POST'])
def delete(username, itemId):
    return 'delete'

if __name__ == '__main__':
    app.secret_key = "secret"
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)