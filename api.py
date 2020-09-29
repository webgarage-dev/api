from flask import Flask, request, make_response
import requests
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "API description"


@app.route("/get-quote", methods=["POST"])
def get_quote():
    api_language_selector = request.args.get("language_selector", "en")
    api_url = f"https://api.forismatic.com/api/1.0/?method=getQuote&lang={api_language_selector}&format=json"
    quote_json = requests.get(api_url).content
    result = make_response(quote_json)
    result.headers['Content-Type'] = 'text/json'
    result.headers['Access-Control-Allow-Origin'] = '*'
    return result
