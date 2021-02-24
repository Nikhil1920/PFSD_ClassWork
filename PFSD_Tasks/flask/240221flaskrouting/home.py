from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


@app.route('/expertise')
def exppertise():
    return render_template('expertise.html')


@app.route('/hobby')
def hobby():
    return render_template('hobby.html')


@app.route('/checkcode')
def checkcode():
    return render_template('checkcode.html')


@app.route('/checkcode', methods=['POST'])
def checkcodestatus():
    usercode = request.form['text']
    with open('code.txt', 'r') as f:
        storedcode = f.read()
    if (usercode == storedcode):
        return 'Your Input code is correct'
    else:
        return 'You have inputed wrong code'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
