from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "myVerifyToken123")

@app.get("/webhook")
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge"), 200
    return "Invalid token", 403

@app.post("/webhook")
def events():
    print("✅ Update received:", request.get_json())
    return "OK", 200

@app.get("/")
def home():
    return "Running", 200
