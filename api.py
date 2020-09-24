from flask import Flask, request
import requests
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/get-quote", methods=["POST"])
def get_quote():
    api_language_selector = request.args.get("language_selector", "en")
    api_url = f"https://api.forismatic.com/api/1.0/?method=getQuote&lang={api_language_selector}&format=json"
    return requests.get(api_url).content
