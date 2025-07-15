import os
import logging
from flask import Flask, request
import telegram

app = Flask(__name__)
TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = telegram.Bot(token=TOKEN)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message_text = update.message.text

    bot.sendMessage(chat_id=chat_id, text="🤖 Auto-response: I received your message!")

    return "ok"

@app.route("/")
def index():
    return "QuizDrop Pro Bot is running!"

if __name__ == "__main__":
    app.run(port=5000)
