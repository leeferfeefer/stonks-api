from app.finnhub import finnhubService
from app.db import bp, db
from flask import Response


@bp.route("/maintenance/symbols/populate", methods=["GET"])
def popuplate_stonk_table():
    stonks = finnhubService.get_stock_symbols()
    for stonk in stonks:
        db.save_stock_symbol(stonk)
    return Response("Stonks added!", status=200, mimetype="text/plain")