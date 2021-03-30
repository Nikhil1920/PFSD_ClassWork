from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    db.create_all()
    return render_template('home.html', title="home_page_title")


@app.route('/insert_data', methods=['post', 'get'])
def insert_data():
    u = User1(id=request.form.get('id'), email=request.form.get(
        'email'), name=request.form.get('name'), authors=request.form.get('authors'))
    db.session.add(u)
    db.session.commit()
    return render_template('insert_data.html', title="insert_page_title")


@app.route('/insert_data2', methods=['post', 'get'])
def insert_data2():
    i = Issuelist(id=request.form.get('bookid'),
                  issue_id=request.form.get('issueid'))
    db.session.add(i)
    db.session.commit()
    return render_template('insert_data.html', title="insert_page_title")


@app.route('/input')
def input():
    return render_template('input.html', title='input_page_title')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/book_details')
def book_details():
    return render_template('book_details.html', books=User1.query)


class User1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.String(100), nullable=True)
    date = db.Column(db.Date, nullable=False, default=datetime.)
    Issuelist
