from flask import Flask, make_response
import requests
import os
app = Flask(__name__)


@app.route("/")
def index():
    return "API description"


# -------------------------- project QUOTES --------------------------

@app.route("/quotes/get/<lang>")
def getquote(lang):
    mode = os.environ.get("WG_API_MODE")
    api_url = f"https://api.forismatic.com/api/1.0/?method=getQuote&lang={lang}&format=json"
    quote_json = requests.get(api_url).content
    result = make_response(quote_json)
    result.headers['Content-Type'] = 'text/json'
    if mode == "debug":
        result.headers['Access-Control-Allow-Origin'] = '*'
    return result


# -------------------------- RUN --------------------------

if __name__ == "__main__":
    app.run()
