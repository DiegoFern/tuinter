from functools import wraps
import os

from flask import (
    Flask,
    jsonify,
    url_for,
    redirect,
    request,
    session)
from flask import render_template as render
from flask import abort

from models import User, Message, db
from list_m import list_messages

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

"""Construct the core application."""
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
Email = ''
Messages = {'': ['h', 'w']}


def is_logged():
    return bool(session.get('email'))


def logged(f):
    @wraps(f)
    def warped(*args, **kwargs):
        if not is_logged():
            return redirect('/')
        return f(*args, **kwargs)
    return warped


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render('login.html')
    if request.method == 'POST':
        if User.query.get(request.form['email']):
            session['email'] = request.form['email']
            session['password'] = request.form['password']
            return redirect('messages')
        else:
            return 'NON VALID'


@app.route('/new_login', methods=['GET', 'POST'])
def new_login():
    if request.method == 'GET':
        return render('new_login.html', **{'error':False})
    if request.method == 'POST':
        if request.form['Email'] and \
                User.query.get(request.form['Email']) is None:
            U = User(
                Name=request.form['Name'],
                Password=request.form['Password'],
                Email=request.form['Email'],
            )
            db.session.add(U)
            db.session.commit()
            session['email'] = request.form['Email']
            return redirect('/messages')

        return render_template('new_login.html', **{'error':True})


        return redirect('messages')
    else:
        return 'NON VALID'

@app.route('/follow',methods=['GET'])
def follow():
    return open('templates/follow.html').read()

@app.route('/api_follow',methods=['GET'])
def follow_api():
    user = User.query.get(session['email'])
    return jsonify({
        'User': user.Name,
        'follows': list(user.Follow),
        'propolsal': [i.json() for i in User.query.filter(User.Email not in user.Follow and User.Email!=user.Email).all()],
    })




@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/messages', methods=['GET'])
def show_messages():
    url_for('static', filename='css/generic.css')
    return open('templates/messages.html').read()



app.route('/list_message', methods=['GET'])( list_messages.get)
app.route('/list_message', methods=['post'])( list_messages.post)
app.route('/list_message', methods=['delete'])( list_messages.delete)



if  __name__=='__main__':
    app.run(debug=True)


