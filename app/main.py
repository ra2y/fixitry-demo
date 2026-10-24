from flask import Flask, jsonify

from app.config import DEMO_PAYMENT_API_KEY


app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "application": "SecureFix Vulnerable Demo",
            "warning": "Intentionally insecure and for local testing only",
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/config-status")
def config_status():
    # The value is never returned. The endpoint only reports whether a value
    # has been configured so the behavior can remain stable after remediation.
    return jsonify({"payment_api_key_configured": bool(DEMO_PAYMENT_API_KEY)})


if __name__ == "__main__":
    # Localhost-only binding keeps the intentionally vulnerable demo private.
    app.run(host="127.0.0.1", port=5000, debug=False)

