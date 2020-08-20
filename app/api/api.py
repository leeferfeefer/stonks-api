from app.api import bp
from flask_cors import cross_origin
from app.finnhub import finnhubService
from app.db import db
from flask import Response, jsonify, request
from app.model import stockSymbol


@bp.route("/stocks/symbols", methods=["GET"])
@cross_origin()
def get_stock_symbols():
    try:
        page_number = request.args.get("pageNumber")
        quantity = request.args.get("quantity")
        query = request.args.get("query")
        if page_number is None or query is None:
            return Response("required value not defined", status=500, mimetype="text/plain")
        if quantity is None:
            return Response("quantity must be defined", status=500, mimetype="text/plain")
        stock_symbol_entities = db.get_stock_symbols_by_query(query, quantity, page_number)
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
    try:
        stock_symbol = request.args.get("stockSymbol")
        if stock_symbol is None:
            return Response("stockSymbol not defined", status=500, mimetype="text/plain")
        return jsonify(finnhubService.get_company_profile(stockSymbol))
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype="text/plain")


@bp.route("/stocks/company/news", methods=["GET"])
@cross_origin()
def get_company_news():
    try:
        stock_symbol = request.args.get("stockSymbol")
        from_date = request.args.get("fromDate")  # "2020-06-01"
        to_date = request.args.get("toDate")  # "2020-06-10"
        if stock_symbol is None or from_date is None or to_date is None:
            return Response("stockSymbol not defined", status=500, mimetype="text/plain")
        return jsonify(finnhubService.get_company_news(stock_symbol, from_date, to_date))
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype="text/plain")


@bp.route("/stocks/company/financials", methods=["GET"])
@cross_origin()
def get_company_financials():
    try:
        stock_symbol = request.args.get("stockSymbol")
        if stock_symbol is None:
            return Response("stockSymbol not defined", status=500, mimetype="text/plain")
        return jsonify(finnhubService.get_company_financials(stock_symbol))
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype="text/plain")


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


# TODO: Convert
# Can also do with foreign exchanges/crypto currencies
@bp.route("/stocks/general_news", methods=["GET"])
@cross_origin()
def get_general_news():
    # Read from DB
    # If not in DB
    # Populate DB with data
    # Return from DB
    return finnhubService.get_general_news()

