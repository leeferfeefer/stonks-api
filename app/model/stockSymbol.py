

def entity_to_dict(stock_symbol_entity):
    stock_symbol_dict = {
        "currency": stock_symbol_entity[1],
        "description": stock_symbol_entity[2],
        "displaySymbol": stock_symbol_entity[3],
        "symbol": stock_symbol_entity[4],
        "type": stock_symbol_entity[5]
    }
    return stock_symbol_dict


def dict_to_entity(stock_symbol_dict):
    return stock_symbol_dict["currency"], stock_symbol_dict["description"], \
           stock_symbol_dict["displaySymbol"], stock_symbol_dict["symbol"], stock_symbol_dict["type"]
