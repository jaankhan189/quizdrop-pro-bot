
import os
import logging
import google.generativeai as genai
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# ===== LOGGING =====
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# ===== CONFIG =====
TELEGRAM_TOKEN = "7718353497:AAFGfbDF2dk79DT4ARuECz6_NTZaB8kiXV0"
GEMINI_API_KEY = "AIzaSyCy8ysazsg44RV3N3cOE0_sHdZ1jdzJx7c"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Optional

CHANNELS = [
    "-1002135188695",  # QuesNotify channel ID (replace with your real channel ID)
    "-1002225131790"   # Detectanza channel ID
]
GROUP_ID = -1002148578851  # Replace with your actual group ID

# ===== INIT APIs =====
genai.configure(api_key=GEMINI_API_KEY)
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

# ===== AI FETCH =====
def get_ai_answers(question):
    answers = {}

    try:
        model = genai.GenerativeModel("gemini-pro")
        gemini_response = model.generate_content(f"Answer this quiz question concisely: {question}")
        answers["Gemini"] = gemini_response.text.strip()
    except Exception as e:
        answers["Gemini"] = f"Gemini Error: {e}"

    try:
        if OPENAI_API_KEY:
            chatgpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Answer this quiz: {question}"}]
            )
            answers["ChatGPT"] = chatgpt_response.choices[0].message.content.strip()
        else:
            answers["ChatGPT"] = "OpenAI key not set"
    except Exception as e:
        answers["ChatGPT"] = f"ChatGPT Error: {e}"

    answers["DeepSeek"] = "B) Cloud Computing"  # Placeholder
    return answers

# ===== HANDLE MSG =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    if "📖" in message or "Question:" in message:
        ai_answers = get_ai_answers(message)

        question_text = message.split("📖")[-1] if "📖" in message else message
        question_text = question_text.strip()

        response = f"""
🧠 *Quiz Answer Detected!*

📖 *Question:*  
{question_text}

🤖 *AI Suggestions:*
♊ Gemini: {ai_answers['Gemini']}
🚀 ChatGPT: {ai_answers['ChatGPT']}
🔍 DeepSeek: {ai_answers['DeepSeek']}

⚠️ *Verify before submitting!*
"""

        for cid in CHANNELS + [GROUP_ID]:
            try:
                await context.bot.send_message(chat_id=cid, text=response, parse_mode="Markdown")
            except Exception as e:
                logging.error(f"Error sending to {cid}: {e}")

# ===== MAIN RUNNER =====
async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("✅ Bot is running...")
    await app.run_polling()

# ===== START =====
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
