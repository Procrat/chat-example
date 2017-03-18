from flask import Flask, render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String)
    content = db.Column(db.String)

    def __repr__(self):
        return 'Message "{}" from "{}"'.format(self.content, self.sender)


db.create_all()


@app.route('/')
def home():
    messages = Message.query.all()
    return render_template('home.html', messages=messages)


@app.route('/post', methods=['POST'])
def receive_message():
    sender = request.form['sender']
    content = request.form['content']
    message = Message(sender=sender, content=content)
    db.session.add(message)
    db.session.commit()
    return redirect('/')