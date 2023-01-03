from flask import Flask
import requests
import json

VITALS_URL = "http://192.168.1.65/api/1/vitals"
METRICS_PREFIX = "tesla_"
VITALS_TO_INCLUDE = [
    "grid_v"
]

app = Flask(__name__)

def fetchVitals():
    res = requests.get(VITALS_URL)
    return json.loads(res.text)

@app.route("/ping")
def ping():
    return "OK"

@app.route("/metrics")
def metrics():
    vitals = fetchVitals()
    metrics = ""
    for k in VITALS_TO_INCLUDE:
        metric_name = METRICS_PREFIX + k
        metric_value = vitals[k]
        metrics += "# TYPE " + metric_name + " gauge" + "\n"
        metrics += metric_name + "{} " + str(metric_value) + "\n"
    return metrics

if __name__ == '__main__':
    app.run()
