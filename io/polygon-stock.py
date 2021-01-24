import requests
from requests.exceptions import HTTPError, Timeout


def __get_per_page__(type: str, perpage: int, page: int):
    print(f"__get_tickers_from_polygon_per_page__(type={type}, perpage={perpage}, page={page})")
    try:
        polygon_url = "https://api.polygon.io"
        api = "/v2/reference/tickers"
        payload = {
            'sort': 'ticker', 
            'type': type,
            # 'market': '',
            # 'locale': '',
            'perpage': perpage,
            'page': page,
            'active': 'true',
            'apiKey': '0kJfuiJORnO7nGk_Sh2EUiOJWeKpT04p',
            }
        timeout = 10
        r = requests.get(polygon_url+api, params=payload, timeout=timeout)
        return r

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')

    except Exception as err:
        print(f'Other error occurred: {err}')


def __get__(type: str):

    perpage = 500
    i = 0
    r_count = 1
    tickerlist = list()

    while ((i * perpage) < r_count):
        i += 1
        r = __get_tickers_from_polygon_per_page__(type, perpage, i)
        rjson = r.json()
        if r_count == 1:
            r_count = int(rjson["count"])
        tickerlist = tickerlist + list((rjson["tickers"]))

    return tickerlist


# Get the daily open, high, low, and close (OHLC) for the entire stocks/equities markets.
def get_Grouped_Daily(date):
    return "/v2/aggs/grouped/locale/us/market/stocks/{date}"


def get_Daily_Open_Close(ticker: str, date):
    return "/v1/open-close/{stocksTicker}/{date}"


# timespan: minute - hour - day - week - month - quarter - year
def get_Aggregates_Bars(ticker: str, multiplier, timespan, from, to):
    return "/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from}/{to}"




