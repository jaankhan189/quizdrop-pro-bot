
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("👋 Welcome to QuizDrop Pro! I am online and ready to help you with quizzes.")

# Create the application and pass your bot token here
app = ApplicationBuilder().token("7718353497:AAFhob8xvYsvl-KiR_KCsf7aSMz0zSFZX-w").build()

# Add command handlers
app.add_handler(CommandHandler("start", start))

# Run the bot
if __name__ == "__main__":
    app.run_polling()
