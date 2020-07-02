from app.api import bp
from flask import Response, request
from flask_cors import cross_origin
# import json
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
def search():
    print(finnhub_client.stock_symbols('US'))
    return Response("", status=200, mimetype='text/plain')

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
