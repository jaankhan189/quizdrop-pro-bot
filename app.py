from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Local answer dictionary (can be expanded)
ANSWER_DB = {
    "common application of NLP": "E) Chatbots/virtual assistants",
    "venture capital funding round": "A) Series C round",
    "goal of data normalization": "C) Reduce data redundancy"
}

@app.route("/", methods=["GET"])
def index():
    return "QuizDrop Pro Bot v2 is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]

        if "text" in message:
            text = message["text"]

            if text == "/start":
                send_message(chat_id, "👋 Welcome to QuizDrop Pro!")
            else:
                reply = find_answer(text)
                send_message(chat_id, reply)

    return {"ok": True}

def find_answer(text):
    for question_keyword in ANSWER_DB:
        if question_keyword.lower() in text.lower():
            return f"✅ Answer: {ANSWER_DB[question_keyword]}"
    return "🤖 This bot will support quizzes soon!"

def send_message(chat_id, text):
    payload = {"chat_id": chat_id, "text": text}
    requests.post(TELEGRAM_API_URL, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
