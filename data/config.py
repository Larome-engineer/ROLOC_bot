import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ADM_ID = os.getenv('ADM_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_PATH = os.getenv("DB_PATH")
FONT_MONO_PATH = os.getenv("FONT_MONO_PATH")
FONT_BOLD_PATH = os.getenv("FONT_BOLD_PATH")
PDF_FORM_SAVE = os.getenv("PDF_TMP_SAVE")
