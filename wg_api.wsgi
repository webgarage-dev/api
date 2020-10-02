import sys
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
sys.path.insert(0, "/srv/www/api.webgarage/")
from wg_api import app as application