#!/usr/bin/python3
"""
    Script that starts a Flask web application
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        You must use the option strict_slashes=False
"""
from flask import Flask
import re

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display “C ”, followed by the value of the text variable"""
    text = re.sub("_", " ", text)
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
