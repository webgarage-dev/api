import sys
import os
from dotenv import load_dotenv
dir_name = os.path.dirname(__file__)
dotenv_path = os.path.join(dir_name, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
sys.path.insert(0, dir_name)
from wg_api import app as application