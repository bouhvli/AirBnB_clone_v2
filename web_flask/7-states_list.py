#!/usr/bin/python3
"""this module will have a
script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_of_the_states():
    """this will list all the states"""
    all_states = sorted(list(storage.all("State").values()),
                        key=lambda st: st.name)
    return (render_template('7-states_list.html', states=all_states))


@app.teardown_appcontext
def close_db(e):
    """and this will close the db"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
