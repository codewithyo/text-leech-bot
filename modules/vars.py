import os

API_ID    = os.environ.get("API_ID", "28583543")
API_HASH  = os.environ.get("API_HASH", "24fd6e53b6034ccbda0bfd62dfd47ad3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8169345673:AAHj8ThzqWNdsSDBmyE0sFlWqOThvPn310E") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
