import requests
import time

# === CONFIG ===
HELIUS_API_KEY = ''  
TELEGRAM_BOT_TOKEN = ''  
TELEGRAM_CHAT_ID = ''  
CHECK_INTERVAL = 60  # How often to check for new coins (in seconds)

# Tracking seen token addresses to avoid duplicate alerts

seen_tokens = set()

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Telegram error: {response.text}")
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")

def fetch_recent_mints():
    url = f"https://api.helius.xyz/v0/addresses/active?api-key={HELIUS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        # Simulating token mints detection for demo purposes
        return data.get("tokens", [])
    except Exception as e:
        print(f"Helius API error: {e}")
        return []

def main():
    print("✅ Meme Coin Watcher is running...\n")
    send_telegram_alert("✅ Meme Coin Watcher is *online* and monitoring new Solana tokens.")

    while True:
        print("🔍 Checking for new meme coins on Solana...")
        new_tokens = fetch_recent_mints()

        for token in new_tokens:
            mint_address = token.get("mint")
            if not mint_address or mint_address in seen_tokens:
                continue

            seen_tokens.add(mint_address)
            name = token.get("name", "Unknown")
            symbol = token.get("symbol", "???")

            message = f"🚀 *New Meme Coin Detected!*\n\n*Name:* {name}\n*Symbol:* {symbol}\n*Mint:* `{mint_address}`"
            send_telegram_alert(message)
            print(f"✅ Alert sent for {name} ({symbol})")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()