
#http://127.0.0.1:3000/api/stock?ticker=KO

import json

from flask import Flask, Response, request
from util import get_last_price

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h2>Hola Ecuador!</h2>"


@app.route("/api/stock")
def get_stock_price():
    company_ticker = request.args.get("ticker")

    try:
        last_price = get_last_price(ticker=company_ticker)
    except ValueError as error:
        return {"company_ticker": company_ticker, "price": None, 'error': str(error)}

    response_raw = {"company_ticker": company_ticker, "price": last_price}

    return Response(json.dumps(response_raw), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)