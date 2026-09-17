# Importing flask & Prometheus 
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # <-- enables / metrics

# Endpoint
@app.route("/")
def hello():
    return "Hello World"

@app.route("/new")
def new():
    return "It's a new world, a new day."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

