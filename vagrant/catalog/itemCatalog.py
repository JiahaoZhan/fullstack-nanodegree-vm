from flask import Flask, render_template, request, redirect, url_for, jsonify, current_app, g
from flask.cli import with_appcontext

app = Flask(__name__)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from databaseSetup import Base, User, Item

engine = create_engine('sqlite:///itemCatalog.db')
Base.metadata.bind = engine


with app.app_context():
    g.user = {
        "username":"admin"
    }

DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)

@app.route('/')
@app.route('/index')
def index():
    items = session.query(Item).all()
    return render_template('index.html', items = items)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    return 'register'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return 'login'

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
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)