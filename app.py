from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

socketio = SocketIO(app)

db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String)
    content = db.Column(db.String)


db.create_all()


@app.route('/')
def home():
    messages = Message.query.all()
    return render_template('home.html', messages=messages)


@socketio.on('new-msg')
def receive_message_through_socket(message_dict):
    message = Message(**message_dict)
    db.session.add(message)
    db.session.commit()
    emit('new-msg', message_dict, broadcast=True)
