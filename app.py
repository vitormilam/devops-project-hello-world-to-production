# Importing flask
from flask import Flask

app = Flask(__name__)

# Endpoint
@app.route("/")
def hello():
    return "Hello World"

@app.route("/new")
def hello():
    return "It's a new world, a new day."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

