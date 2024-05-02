from flask import Flask, render_template, request #flask import
from random import randrange

import sys

app = Flask(__name__) # to initiate this for web app

@app.route("/")
def index():
    randindex = randrange(2)

    return render_template("index.html", status = "asdmessage")
