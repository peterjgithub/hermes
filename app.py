from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from urllib.request import urlopen
from datetime import date, datetime
import json
from dotenv import load_dotenv
import os
import requests
from requests.exceptions import HTTPError, Timeout
# BDay is business day, not birthday...
from pandas.tseries.offsets import BDay
from pandas import pandas as pd

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

from models import Quote

today = date.today()    
_tdate = str(today)


def get_url_content(url: str):
    _true_url = url.replace('"', "")
    with urlopen(_true_url) as response:
        source = response.read()
    jsondata = json.loads(source)
    return jsondata


def __get_Grouped_Daily_Bars__(from_date: date):
    _beginning_date = str(from_date)
    print(f"__get_Grouped_Daily_Bars__(from_date={_beginning_date})")

    try:
        polygon_url = "https://api.polygon.io"
        api = "/v2/aggs/grouped/locale/us/market/stocks/" + _beginning_date
        payload = {
            'unadjusted': "false",
            'apiKey': '0kJfuiJORnO7nGk_Sh2EUiOJWeKpT04p',
            }
        timeout = 10
        r = requests.get(polygon_url+api, params=payload, timeout=timeout)
        rjson = r.json()
        # resultlist = list(rjson["results"])
        return rjson

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')

    except Exception as err:
        print(f'Other error occurred: {err}')


# Get the daily open, high, low, and close (OHLC) for the entire stocks/equities markets.
def get_Grouped_Daily_Bars(from_date: date):
    last_business_day = date.today() - BDay(1)
    from_date = from_date if from_date is not None else last_business_day
    jsonresponse = __get_Grouped_Daily_Bars__(from_date)
    return jsonresponse


@app.route("/updates")
def updates():
    jsontxt = get_Grouped_Daily_Bars(date(2021,1,21))
    source = jsontxt["results"]
    print("look here!!!!")
    for quote in source:
        quote['t'] = pd.to_datetime(quote['t'], infer_datetime_format=True)
    return render_template("updates.html", source=source)


@app.route("/")
def home():
    apiKey = os.getenv("POLYGON_APIKEY")
    url_core = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-11-01/"
    url = f"{url_core}{_tdate}?apiKey={apiKey}"    
    content = get_url_content(url)
    aapl_data = content["results"]
    return render_template("home.html", source=aapl_data)


@app.route("/exchanges")
def exchanges():
    url = 'https://api.polygon.io/v1/meta/exchanges?apiKey=0kJfuiJORnO7nGk_Sh2EUiOJWeKpT04p'
    content = get_url_content(url)
    return render_template("stockexchanges.html", source_to_html_from_app=content)


@app.route("/tickers")
def tickers():
    url = 'https://api.polygon.io/v2/reference/tickers?sort=ticker&type=cs&perpage=20&page=1&apiKey=0kJfuiJORnO7nGk_Sh2EUiOJWeKpT04p'
    content = get_url_content(url)
    mytickers = content["tickers"]
    return render_template("tickers.html", source=mytickers)

if __name__ == "__main__":
    app.run()