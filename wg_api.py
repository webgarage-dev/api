from flask import Flask, make_response
import requests
app = Flask(__name__)


@app.route("/")
def index():
    return "API description"


# -------------------------- project QUOTES --------------------------

@app.route("/quotes/get/<lang>")
def getquote(lang):
    api_url = f"https://api.forismatic.com/api/1.0/?method=getQuote&lang={lang}&format=json"
    quote_json = requests.get(api_url).content
    result = make_response(quote_json)
    result.headers['Content-Type'] = 'text/json'
    result.headers['Access-Control-Allow-Origin'] = '*'
    return result


if __name__ == "__main__":
    app.run()
