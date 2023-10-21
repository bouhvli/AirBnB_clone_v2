#!/usr/bin/python3
"""this module will have a
script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def list_of_the_states(state_id=None):
    """this will list all the states"""
    all_states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return (render_template('9-states.html',
                            states=all_states,
                            state_id=state_id))


@app.teardown_appcontext
def close_db(e):
    """and this will close the db"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
