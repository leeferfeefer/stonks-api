from app.finnhub import finnhub_client
from flask import Response, request, jsonify


def get_stock_symbols():
    return finnhub_client.stock_symbols("US")


def get_company_profile(stock_symbol):
    return finnhub_client.company_profile2(symbol=stock_symbol)


def get_company_news(stock_symbol, from_date, to_date):
    return finnhub_client.company_news(stock_symbol, _from=from_date, to=to_date)


def get_company_financials(stock_symbol):
    return finnhub_client.company_basic_financials(stock_symbol, 'all')


# TODO: Convert
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
        # return Response("Unknown server error", status=500, mimetype="text/plain")
        return None

