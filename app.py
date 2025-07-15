import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Hello {user.first_name}!
Welcome to *QuizDrop Pro Bot*.
Use /help to view available features.",
        parse_mode='Markdown'
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 Available Commands:
"
        "/start - Show welcome message
"
        "/help - Show this help menu"
    )

# Generic message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    await update.message.reply_text(f"You said: {message}")

# Main entry
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running...")
    app.run_polling()