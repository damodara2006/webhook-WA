from flask import Flask, request
import os

app = Flask(__name__)
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "myVerifyToken123")

@app.route("/webhook", methods=["GET", "POST"], strict_slashes=False)
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Invalid token", 403

    print("✅ WEBHOOK HIT:", request.data.decode("utf-8"))
    return "OK", 200


@app.get("/")
def home():
    return "Running", 200
