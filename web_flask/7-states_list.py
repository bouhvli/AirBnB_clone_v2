#!/usr/bin/python3
""""""
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_of_the_states():
    """"""
    all_states = sorted(list(storage.all("State").values()),
                        key=lambda st: st.name)
    return (render_template('7-states_list.html', states=all_states))


@app.teardown_appcontext
def close_db(e):
    """"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
