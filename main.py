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

@app.get("/privacy")
def privacy():
    return """
    <html>
      <head><title>Privacy Policy</title></head>
      <body>
        <h1>Privacy Policy</h1>
        <p>This app uses WhatsApp Cloud API to receive and send messages.</p>
        <p>We may temporarily process message content to generate automated replies.</p>
        <p>We do not sell or share user data with third parties.</p>
        <p>Data is used only to provide support responses and improve the service.</p>

        <h2>Data Retention</h2>
        <p>Messages may be stored for debugging and support purposes.</p>

        <h2>User Rights</h2>
        <p>Users can request deletion of their data using the delete-data page.</p>

        <h2>Contact</h2>
        <p>Email: damodara2006@gmail.com</p>
      </body>
    </html>
    """, 200


@app.get("/terms")
def terms():
    return "Terms of Service - Test App", 200

@app.get("/delete-data")
def delete_data():
    return "To delete your data, contact: damodara2006@gmail.com", 200


@app.get("/")
def home():
    return "Running", 200
