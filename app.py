from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7718353497:AAF7FPXt_8jx0F7eDWIkGZe_yzlHG3fWKqs"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def index():
    return "QuizDrop Pro Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        if text == "/start":
            send_message(chat_id, "👋 Welcome to QuizDrop Pro!")
        else:
            send_message(chat_id, "🤖 This bot will support quizzes soon!")

    return {"status": "ok"}

def send_message(chat_id, text):
    payload = {"chat_id": chat_id, "text": text}
    requests.post(TELEGRAM_API_URL, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
