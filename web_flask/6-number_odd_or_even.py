#!/usr/bin/python3
"""
    Script that starts a Flask web application
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        You must use the option strict_slashes=False
"""
from flask import Flask, render_template
import re

app = Flask(__name__, template_folder="templates")


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


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """isplay “Python ”, followed by the value of the text"""
    text = re.sub("_", " ", text)
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display “n is a number” only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display “n is a number” only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
