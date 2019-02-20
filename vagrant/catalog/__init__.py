from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'index'


@app.route('/login', methods = ['GET', 'POST'])
def login():
    return 'login'

@app.route('/user/<string:username>/index')
def userIndex(username):
    return 'userIndex'

@app.route('/user/<string:username>/add', methods = ['GET', 'POST'])
def add(username):
    return 'add'

@app.route('/user/<string:username>/<int:itemId>/edit', methods = ['GET', 'POST'])
def edit(username, itemId):
    return 'edit'

@app.route('/user/<string:username>/<int:itemId>/delete', methods = ['GET', 'POST'])
def delete(username, itemId):
    return 'delete'

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1', port = 5000)