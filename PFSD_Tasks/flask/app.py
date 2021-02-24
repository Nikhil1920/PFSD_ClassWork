from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/welcome')
def welcome():
    return '<h1>Welcome to welcome page</h1>'


@app.route('/login')
def login():
    return '<h1>Welcome to login page</h1>'


@app.route('/logout')
def logout():
    return '<h1>Welcome to logout page</h1>'


@app.route('/register')
def register():
    return '<h1>Welcome to register page</h1>'


@app.route('/aboutus')
def aboutus():
    return '<h1>Welcome to aboutus page</h1>'
