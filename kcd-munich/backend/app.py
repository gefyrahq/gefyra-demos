from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/color")
def color():
    return jsonify({"color": "green"})

