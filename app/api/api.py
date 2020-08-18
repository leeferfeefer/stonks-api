from app.api import bp
from flask import Response, request, jsonify
from flask_cors import cross_origin
import finnhub
import os

finnhub_client = finnhub.Client(api_key=os.environ["STONK_API_KEY"])


@bp.route("/stocks/symbols", methods=["GET"])
@cross_origin()
def get_stock_symbols():
    try:
        stock_symbols_response = finnhub_client.stock_symbols("US")[0:25]
        return jsonify(stock_symbols_response)
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
        company_profile_response = finnhub_client.company_profile2(symbol=stock_symbol)
        return jsonify(company_profile_response)
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
        company_news_response = finnhub_client.company_news(stock_symbol, _from=from_date, to=to_date)
        return jsonify(company_news_response)
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
        company_financials_response = finnhub_client.company_basic_financials(stock_symbol, 'all')
        return jsonify(company_financials_response.to_dict())
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype="text/plain")


# Need Premium subscription :(
@bp.route("/stocks/tick/data", methods=["GET"])
@cross_origin()
def get_tick_data():
    try:
        stock_symbol = request.args.get("stockSymbol")
        if stock_symbol is None:
            return Response("stockSymbol not defined", status=500, mimetype="text/plain")
        tick_data_response = finnhub_client.stock_tick('AAPL', '2020-03-25', 500, 0)
        print(tick_data_response)
        return jsonify(tick_data_response.to_dict())
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype="text/plain")


# Can also do with foreign exchanges/crypto currencies
@bp.route("/stocks/general_news", methods=["GET"])
@cross_origin()
def get_general_news():
    try:
        general_news_response = finnhub_client.general_news('general', min_id=0)
        print(general_news_response)
        newsArray = []
        for general_news in general_news_response:
            news = {"category": general_news.category, "datetime": general_news.datetime,
                    "headline": general_news.headline, "id": general_news.id, "image": general_news.image,
                    "related": general_news.related, "source": general_news.source, "summary": general_news.summary,
                    "url": general_news.url}
            newsArray.append(news)
        return jsonify(newsArray)
    except Exception as e:
        print(e)
        return Response("Unknown server error", status=500, mimetype="text/plain")
