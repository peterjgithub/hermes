import requests
from requests.exceptions import HTTPError, Timeout


def __get_tickers_from_polygon_per_page__(type: str, perpage: int, page: int):
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


def __get_tickers_from_polygon__(type: str):

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


def get_CS_common_stock_tickers():
    return __get_tickers_from_polygon__("CS")


def get_INDEX_tickers():
    return __get_tickers_from_polygon__("INDEX")


def get_ETF_exchang_traded_fund_tickers():
    return __get_tickers_from_polygon__("ETF")


# types": {
#    "CS": "Common Stock",
#    "ADR": "American Depository Receipt",
#    "NVDR": "Non-Voting Depository Receipt",
#    "GDR": "Global Depositary Receipt",
#    "SDR": "Special Drawing Right",
#    "CEF": "Closed-End Fund",
#    "ETP": "Exchange Traded Product/Fund",
#    "REIT": "Real Estate Investment Trust",
#    "MLP": "Master Limited Partnership",
#    "WRT": "Equity WRT",
#    "PUB": "Public",
#    "NYRS": "New York Registry Shares",
#    "UNIT": "Unit",
#    "RIGHT": "Right",
#    "TRAK": "Tracking stock or targeted stock",
#    "LTDP": "Limited Partnership",
#    "RYLT": "Royalty Trust",
#    "MF": "Mutual Fund",
#    "PFD": "Preferred Stock",
#    "FDR": "Foreign Ordinary Shares",
#    "OST": "Other Security Type",
#    "FUND": "Fund",
#    "SP": "Structured Product",
#    "SI": "Secondary Issue"
#   },
#   "indexTypes": {
#    "INDEX": "Index",
#    "ETF": "Exchange Traded Fund (ETF)",
#    "ETN": "Exchange Traded Note (ETN)",
#    "ETMF": "Exchange Traded Managed Fund (ETMF)",
#    "SETTLEMENT": "Settlement",
#    "SPOT": "Spot",
#    "SUBPROD": "Subordinated product",
#    "WC": "World Currency",
#    "ALPHAINDEX": "Alpha Index"
#   }


# Get details for a ticker symbol's company/entity. 
# This provides a general overview of the entity with information 
# such as name, sector, exchange, logo and similar companies.
def get_Ticker_Details(ticker: str):
    return "/v1/meta/symbols/{stocksTicker}/company"


def get_Stock_Splits(ticker: str):
    return "/v2/reference/splits/{stocksTicker}"


def get_Stock_Dividends(ticker: str):
    return "/v2/reference/dividends/{stocksTicker}"


# Get historical financial data for a stock ticker.
def get_Stock_Financials(ticker: str):
    return "/v2/reference/financials/{stocksTicker}"


def get_Upcoming_market_holidays():
    return "/v1/marketstatus/upcoming"


def get_Market_Status():
    return "/v1/marketstatus/now"
