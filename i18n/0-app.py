#!/usr/bin/env python3
"""0-app.py"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    """hello_world"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
