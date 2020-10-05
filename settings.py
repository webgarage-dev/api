import os
from dotenv import load_dotenv
dir_name = os.path.dirname(__file__)
dotenv_path = os.path.join(dir_name, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

os_environ = os.environ

WG_API_MODE = os_environ.get("WG_API_MODE")
WG_CORS_DOMAIN = os_environ.get("WG_CORS_DOMAIN")
UNSPLASH_ACCOUNT_KEY = os_environ.get("UNSPLASH_ACCOUNT_KEY")

