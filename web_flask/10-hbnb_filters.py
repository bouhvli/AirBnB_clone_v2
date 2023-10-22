#!/usr/bin/python3
"""this module will have a
script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def search_filter(state_id=None):
    """this will list all the states"""
    all_states = storage.all("State").values()
    all_amenities = storage.all("Amenity").values()
    return (render_template('10-hbnb_filters.html',
                            states=all_states,
                            amenities=all_amenities))


@app.teardown_appcontext
def close_db(e):
    """and this will close the db"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
