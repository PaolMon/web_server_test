from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
SERVER_PORT = os.getenv("SERVER_PORT")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=SERVER_PORT)