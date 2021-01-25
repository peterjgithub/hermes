from datetime import date 
import requests
from requests.exceptions import HTTPError, Timeout
from flask import Flask, render_template
# BDay is business day, not birthday...
from pandas.tseries.offsets import BDay
from pandas import pandas as pd

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



