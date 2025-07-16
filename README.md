# QuizDrop AI Bot 🤖

This Telegram bot detects quiz questions and automatically provides AI-generated answers using Gemini and ChatGPT.

## Features
- Detects messages containing quiz questions
- Uses Gemini Pro API to generate answers
- Optionally uses OpenAI ChatGPT (if API key is provided)
- Sends answers to multiple channels and group

## Setup Instructions

### 1. Clone the repo or upload files
Upload to GitHub or Replit.

### 2. Add your secrets
Use Replit Secrets or `.env`:
- `OPENAI_API_KEY` (optional if using ChatGPT)
- Bot token and Gemini are already hardcoded. Change if needed.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the bot
```bash
python main.py
```

## Notes
- Make sure your bot is admin in the channels and group.
- Replace dummy `CHANNELS` and `GROUP_ID` if needed.

