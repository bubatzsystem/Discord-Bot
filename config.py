import os
from dotenv.main import load_dotenv

load_dotenv()

# Bot setup
PREFIX = "!"
BOT_NAME = "Morty Bot"
BOT_TOKEN = os.getenv("BOT_TOKEN", "")