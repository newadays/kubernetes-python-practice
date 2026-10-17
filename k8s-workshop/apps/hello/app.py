"""hello: the application service. Python 'hello'.

Routes: / (public), /healthz, /readiness, /version
"""
import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "1.0.0")
JWT_SECRET = os.environ.get("JWT_SECRET", "change-me")  # injected from a Kubernetes Secret
print(f"JWT_SECRET: {JWT_SECRET}")

@app.route("/")
def hello_world():
    return "<p>Hello, World - from the Gbenga service - updated!</p>" + JWT_SECRET

@app.get("/healthz")
def healthz():
    return "ok"


@app.get("/readiness")
def readiness():
    return "ok"


@app.get("/version")
def version():
    return jsonify(version=VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
