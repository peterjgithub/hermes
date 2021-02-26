from flask import Blueprint, render_template
from datetime import date, datetime, timedelta
from polygon import RESTClient 
from app.models import db, Quote, get_aapl_quotes, save_quotes
import os
import uuid

print("initiate tickers-route.py")

tickers_bp = Blueprint(
    "tickers_bp", 
    __name__, 
    template_folder='templates'
    )

apiKey = os.environ.get("POLYGON_APIKEY")

def ts_to_datetime(ts) -> str:
    return datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def ts_to_date(ts) -> str:
    return date.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d')


@tickers_bp.route("/")
def tickers():
    with RESTClient(apiKey) as client:
        resp = client.reference_tickers(sort='ticker')
        mytickers = resp.tickers
    return render_template("tickers.html", source=mytickers)


@tickers_bp.route("/updates")
def updates():
    with RESTClient(apiKey) as client:
        return7days = (datetime.now() - timedelta(days=1)).date()
        # return7days = (datetime.now() - timedelta(days=20)).date()
        response = client.stocks_equities_grouped_daily('us', 'stocks', return7days, unadjusted=True)
    api_results = response.results
    quotes = list()
    for result in api_results:
        quotes.append(Quote(
            id=uuid.uuid4(),
            ticker=result.get('T'),
            volume=result.get('v'),
            volume_weighted_avg_price=result.get('vw'),
            open=result.get('o'),
            adj_close=result.get('c'),
            close=result.get('c'),
            high=result.get('h'),
            low=result.get('l'),
            date_time=ts_to_date(result.get('t')),                
            )
        )
    save_quotes(quotes)
    return render_template("updates.html", source=quotes)


@tickers_bp.route("/aapl")
def aapl():
    # newquote = Quote(
    #     id = uuid.uuid4(),
    #     ticker = "AAPL",
    #     date_time = datetime(2020,11,2,22,0), 
    #     open = 109.11, 
    #     high = 110.68, 
    #     low = 107.32, 
    #     close = 108.77, 
    #     adj_close = 108.77, 
    #     volume = 122712099.0, 
    #     volume_weighted_avg_price = 108.6262
    # )
    # session = db.session
    # session.add(newquote)
    # session.commit()

    quotes = get_aapl_quotes()

    # with RESTClient(apiKey) as client:
    #     resp = client.stocks_equities_aggregates('AAPL', 1, 'day', date(2020,11,1), date.today())
    #     quotes = resp.results
    #     for quote in quotes:
    #         quote['t'] = ts_to_date(quote['t'])
    return render_template("aapl.html", source=quotes)


# if __name__ == "__main__":
#     print("initiate views- __name==__main__")
#     app.run()
