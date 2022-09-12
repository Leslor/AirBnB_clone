#!/usr/bin/python3
"""
    Script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """: display a HTML page: (inside the tag BODY"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_appcontext(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
