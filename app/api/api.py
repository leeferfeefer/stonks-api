from app.api import bp
from flask import Response, request
from flask_cors import cross_origin
# import json


@bp.route('/', methods=['GET'])
@cross_origin()
def search():
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
