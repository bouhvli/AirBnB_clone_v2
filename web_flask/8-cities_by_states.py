#!/usr/bin/python3
"""this module will have a
script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_of_the_states():
    """this will list all the states"""
    all_states = storage.all("State").values()
    return (render_template('8-cities_by_states.html', states=all_states))


@app.teardown_appcontext
def close_db(e):
    """and this will close the db"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
