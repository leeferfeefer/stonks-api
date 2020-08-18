from app.api import bp
from flask_cors import cross_origin
from app.finnhub import finnhubService
from app.db import db
from flask import Response, jsonify
from app.model import stockSymbol

@bp.route("/stocks/symbols", methods=["GET"])
@cross_origin()
def get_stock_symbols():
    try:
        stock_symbol_entities = db.get_stock_symbols()
        stock_symbols = []
        for stock_symbol_entity in stock_symbol_entities:
            stock_symbols.append(stockSymbol.entity_to_dict(stock_symbol_entity))
        return jsonify(stock_symbols)
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype="text/plain")


@bp.route("/stocks/company/profile", methods=["GET"])
@cross_origin()
def get_company_profile():
    # Read from DB
    # If not in DB
    # Populate DB with data
    # Return from DB
    return finnhubService.get_company_profile()


@bp.route("/stocks/company/news", methods=["GET"])
@cross_origin()
def get_company_news():
    # Read from DB
    # If not in DB
    # Populate DB with data
    # Return from DB
    return finnhubService.get_company_news()


@bp.route("/stocks/company/financials", methods=["GET"])
@cross_origin()
def get_company_financials():
    # Read from DB
    # If not in DB
    # Populate DB with data
    # Return from DB
    return finnhubService.get_company_financials()


# Need Premium subscription :(
# @bp.route("/stocks/tick/data", methods=["GET"])
# @cross_origin()
# def get_tick_data():
#     try:
#         stock_symbol = request.args.get("stockSymbol")
#         if stock_symbol is None:
#             return Response("stockSymbol not defined", status=500, mimetype="text/plain")
#         tick_data_response = finnhub_client.stock_tick('AAPL', '2020-03-25', 500, 0)
#         print(tick_data_response)
#         return jsonify(tick_data_response.to_dict())
#     except Exception as e:
#         print(e)
#         return Response("Unknown server error", status=500, mimetype="text/plain")


# Can also do with foreign exchanges/crypto currencies
@bp.route("/stocks/general_news", methods=["GET"])
@cross_origin()
def get_general_news():
    # Read from DB
    # If not in DB
    # Populate DB with data
    # Return from DB
    return finnhubService.get_general_news()

