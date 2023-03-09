"""
Hello world application of Flask
Command - `flask --app main run`
- HOME URL
https://swapi.dev
http://127.0.0.1:5000
- RELATIVE
/api/films
- ABSOLUTE URL
"""

from flask import Flask


# `Flask` is a class we use to instantiate an application
app = Flask(__name__)


# First http GET request
@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


# SECOND http GET request
@app.route("/greeting")
def custom_message():

    import requests
    list1 = []

    response = requests.get("https://swapi.dev/api/people/1/")

    list1.append(response)
    # store response in DB
    print(list1)

