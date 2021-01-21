from flask import Flask, render_template
import json
from urllib.request import urlopen
import datetime
from datetime import date

app = Flask(__name__)


today = date.today()
_tdate = str(today)
url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/minute/2020-11-01/"'+_tdate+'"?apiKey=HBSH9Fc30LZbumAvQXssFHbqw8jBgoeEcI3nTe' 
_true_url = url.replace('"', "")
with urlopen(_true_url) as response: 
	source = response.read()
data = json.loads(source)
print(source)

@app.route("/")
def function():
	return render_template("home.html",source_to_html_from_app = source)
if __name__ == "__main__": 
	app.run()