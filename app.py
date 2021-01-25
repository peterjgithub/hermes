from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from urllib.request import urlopen
from datetime import date, datetime
from polygon import RESTClient 
from dotenv import load_dotenv
# from models import Quote
import os

load_dotenv()
apiKey = os.getenv("POLYGON_APIKEY")

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


def ts_to_datetime(ts) -> str:
    return datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def ts_to_date(ts) -> str:
    return date.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d')


@app.route("/")
def tickers():
    with RESTClient(apiKey) as client:
        resp = client.reference_tickers(sort='ticker')
        mytickers = resp.tickers
    return render_template("tickers.html", source=mytickers)


@app.route("/updates")
def updates():
    with RESTClient(apiKey) as client:
        resp = client.stocks_equities_grouped_daily('us', 'stocks', date(2021,1,22))
        quotes = resp.results
        for quote in quotes:
            quote['t'] = ts_to_date(quote['t'])
    return render_template("updates.html", source=quotes)


@app.route("/aapl")
def aapl():
    with RESTClient(apiKey) as client:
        resp = client.stocks_equities_aggregates('AAPL', 1, 'day', date(2020,11,1), date.today())
        quotes = resp.results
        for quote in quotes:
            quote['t'] = ts_to_date(quote['t'])
    return render_template("aapl.html", source=quotes)


if __name__ == "__main__":
    app.run()
