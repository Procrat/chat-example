Naive chat application
======================

This is a small persistent, real-time chat web application using [Flask](http://flask.pocoo.org/) and [SocketIO](https://flask-socketio.readthedocs.io/en/latest/).
Its reason of existence is for use during a [thunder talk](https://www.meetup.com/Enspiral-Dev-Academy-Meetup/events/238431831/) at [Enspiral Dev Academy Meetup](https://www.meetup.com/Enspiral-Dev-Academy-Meetup/) as an introduction to Python for people with a web development background.


Usage
-----

Set up [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/):
```python
virtualenv .env
. .env/bin/activate
pip install -r requirements
```

Run (with virtualenv activated):
```python
FLASK_APP=app.py flask run
```
