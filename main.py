from flask import Flask, request
import os

app = Flask(__name__)
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "myVerifyToken123")

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    # ✅ Verify
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Invalid token", 403

    # ✅ Receive all events (messages + statuses)
    data = request.get_json(silent=True)
    print("✅ WEBHOOK RECEIVED:", data)
    return "OK", 200

@app.get("/")
def home():
    return "Running", 200
