from flask import Flask, render_template, request, redirect, make_response
import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return {"HimajinAPI": "Created by Kenji"}

if __name__ == '__main__':
    app.run(host="0.0.0.0")