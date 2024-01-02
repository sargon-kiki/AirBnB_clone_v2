#!/usr/bin/python3

""" Starts the flask Applications

The application listens on all interface 0.0.0.0
on port 5000

Routes:
    /: Shows 'Hello HBNB!'
 """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def show_hbnb():
    """Displays 'Hello HBNB'"""
    return "Hello HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
