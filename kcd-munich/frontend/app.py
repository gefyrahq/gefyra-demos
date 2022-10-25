import os

import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def frontend():
    SVC = os.environ.get("SVC_URL")

    response = requests.get(f"http://{SVC}/color")
    color = response.json()["color"]
    return f"<h1 style='background-color: {color};'>Hello KCD!</h1>"

