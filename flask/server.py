from flask import Flask
import os

app = Flask(__name__)


@app.route("/home")
def hello():
    return "<p><h1>Hello World!</h1></p><p>hello hello hello</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
