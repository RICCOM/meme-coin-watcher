## 🐸 Solana Meme Coin Watcher

A simple Python bot that monitors the Solana blockchain for newly launched meme coins and sends real-time alerts to a Telegram chat.

## 🚀 Features

- Monitors Solana for new token mints (meme coins)
- Sends instant alerts to Telegram
- 24/7 monitoring when deployed on cloud platforms like Replit or Render

---

## 🔧 Requirements

- Python 3.7+
- Helius API Key (get one from [helius.xyz](https://www.helius.xyz/))
- Telegram Bot Token (created using [BotFather](https://t.me/BotFather))
- Telegram Chat ID (from your Telegram account)

---

## 📦 Installation

1. **Clone the repo** or copy the script:
   ```bash
   git clone https://github.com/RICCOM/meme-watcher.git
   cd solana-meme-watcher
# Install dependencies:

pip install -r requirements.txt
Set environment variables (in .env or directly in the code):

HELIUS_API_KEY=your_helius_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
# 🧪 Running the bot

python solana_meme_alert.py
You should see:


✅ Meme Coin Watcher is running...
🔍 Checking for new meme coins on Solana...
☁️ Deployment
You can deploy this bot on platforms like:

Replit – easiest for beginners

Render – best for background workers

# ✅ Example Alert

🚀 New Meme Coin Detected!

Name: Wojak Coin  
Symbol: $WOJ  
Mint: Fk3x...2kHj
# 🛠 Future Improvements
Filter only trending or high-volume meme coins

Add support for webhook integrations

Store discovered tokens in a database

# 📄 License
MIT License. Feel free to fork and build on this!

Made with ❤️ to help you never miss a meme coin launch on Solana.
