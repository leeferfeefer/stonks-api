from app.api import bp
from flask import Response, request, jsonify
from flask_cors import cross_origin
import json
import finnhub
import os

configuration = finnhub.Configuration(
    api_key={
        'token': os.environ['STONK_API_KEY']
    }
)
finnhub_client = finnhub.DefaultApi(finnhub.ApiClient(configuration))


@bp.route('/stocks/symbols', methods=['GET'])
@cross_origin()
def stock_symbols():
    try:
        stock_symbols_response = finnhub_client.stock_symbols('US')
        stock_symbols = []
        for stock in stock_symbols_response:
            stock_symbol = {}
            stock_symbol['description'] = stock.description
            stock_symbol['display_symbol'] = stock.display_symbol
            stock_symbol['symbol'] = stock.symbol
            stock_symbols.append(stock_symbol)
        return jsonify(stock_symbols)
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype='text/plain')


@bp.route('/company/profile', methods=['GET'])
@cross_origin()
def company_profile():
    try:
        stock_symbol = request.args.get('stockSymbol')
        if stock_symbol is None:
            return Response("stockSymbol not defined", status=500, mimetype='text/plain')
        company_profile_response = finnhub_client.company_profile2(symbol=stock_symbol)
        print(company_profile_response)
        return jsonify(company_profile_response.to_dict())
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype='text/plain')
#
# @bp.route('/keypress', methods=['POST'])
# @cross_origin()
# def keyPress():
#     try:
#         data = request.get_json() or {}
#         address = data['address']
#         keypress = data['keypress']
#         sendKeyPress(address, keypress)
#         return Response("", status=200, mimetype='text/plain')
#     except:
#         return Response("", status=400, mimetype='text/plain')
