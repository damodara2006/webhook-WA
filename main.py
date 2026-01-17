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
    data = request.get_json()

    try:
        value = data["entry"][0]["changes"][0]["value"]
        name = value["contacts"][0]["profile"]["name"]
        wa_id = value["contacts"][0]["wa_id"]
        text = value["messages"][0]["text"]["body"]

        print(f"✅ New message from {name} ({wa_id}): {text}")

    except Exception as e:
        print("⚠️ Unknown webhook format:", data)

    return "OK", 200

@app.get("/")
def home():
    return "Running", 200
