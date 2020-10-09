import requests
import json
from flask import Flask, make_response, jsonify
from settings import WG_API_MODE, WG_CORS_DOMAIN, UNSPLASH_ACCESS_KEY
app = Flask(__name__)


@app.route("/")
def index():
    return "API description here"


# -------------------------- project QUOTES --------------------------


@app.route("/quotes/get/<lang>")
def getquote(lang):
    api_url = f"https://api.forismatic.com/api/1.0/?method=getQuote&lang={lang}&format=json"
    quote_dict = json.loads(requests.get(api_url).content)
    result_dict = {
        "quoteText": quote_dict.get("quoteText"),
        "quoteAuthor": quote_dict.get("quoteAuthor")
    }
    result = make_response(jsonify(result_dict))
    result.headers['Content-Type'] = 'text/json'
    if WG_API_MODE == "debug":
        result.headers['Access-Control-Allow-Origin'] = "*"
    else:
        result.headers['Access-Control-Allow-Origin'] = WG_CORS_DOMAIN
    return result


# -------------------------- project UNSPLASH QUOTES --------------------------

@app.route("/uninfscroll/photos/get")
def get_photos():
    count = 30
    api_url = f"https://api.unsplash.com/photos/random/?client_id={UNSPLASH_ACCESS_KEY}&count={count}"
    print(api_url)
    result = make_response(requests.get(api_url).content)
    if WG_API_MODE == "debug":
        result.headers['Access-Control-Allow-Origin'] = "*"
    else:
        result.headers['Access-Control-Allow-Origin'] = WG_CORS_DOMAIN
    return result

# -------------------------- RUN --------------------------


if __name__ == "__main__":
    app.run()
