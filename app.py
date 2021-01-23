from flask import Flask, render_template
from urllib.request import urlopen
from datetime import date
import json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
today = date.today()    
_tdate = str(today)


def get_url_content(url: str):
    _true_url = url.replace('"', "")
    with urlopen(_true_url) as response:
        source = response.read()
    jsondata = json.loads(source)
    return jsondata


@app.route("/")
def home():
    url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/minute/2020-11-01/"' + _tdate + '"?apiKey=HBSH9Fc30LZbumAvQXssFHbqw8jBgoeEcI3nTe'
    content = get_url_content(url)
    return render_template("home.html", source_to_html_from_app=content)


@app.route("/exchanges")
def exchanges():
    url = 'https://api.polygon.io/v1/meta/exchanges?apiKey=0kJfuiJORnO7nGk_Sh2EUiOJWeKpT04p'
    content = get_url_content(url)
    return render_template("stockexchanges.html", source_to_html_from_app=content)


@app.route("/tickers")
def tickers():
    url = 'https://api.polygon.io/v2/reference/tickers?sort=ticker&type=cs&perpage=5&page=1&apiKey=0kJfuiJORnO7nGk_Sh2EUiOJWeKpT04p'
    content = get_url_content(url)
    mytickers = content["tickers"]
    return render_template("tickers.html", source=mytickers)


if __name__ == "__main__":
    app.run()