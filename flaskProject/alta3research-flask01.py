#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from random import randint
import json

app = Flask(__name__)

dummyDB = [
    {'name': 'Paul Atreides', 'affiliations': ['House Atreides', 'the Fremen', 'the Imperial Family'], 'books': ['Dune', 'Dune Messiah', 'Children of Dune']},
    {'name': 'Leto Atreides', 'affiliations': ['House Atreides'], 'books': ['Dune']},
    {'name': 'Shadout Mapes', 'affiliations': ['House Atreides', 'the Fremen'], 'books': ['Dune']},
    {'name': 'Piter De Vries', 'affiliations': ['House Harkonnen'], 'books': ['Dune']},
    {'name': 'Duncan Idaho', 'affiliations': ['House Atreides', 'the Bene Telilax', 'the Bene Gesserit', 'the Honored Matres'], 'books': ['Dune', 'Dune Messiah', 'Children of Dune', 'God Emperor of Dune', 'Heretics of Dune', 'Chapterhouse: Dune']}
]


@app.route("/")
def help():
    return render_template("help.html", address = url_for('returnJson'))


@app.route("/rand_character")
def returnJson():
    return json.dumps(dummyDB[randint(0, len(dummyDB) - 1)])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application
