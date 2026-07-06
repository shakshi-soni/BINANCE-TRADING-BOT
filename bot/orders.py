import logging
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger("trading_bot")

def place_futures_order(client, params: dict):
    """Sends the order request to the Binance Futures Testnet endpoint."""
    try:
        logger.info(f"Sending API request to Binance Testnet with params: {params}")

        order_args = {
            "symbol": params["symbol"],
            "side": params["side"],
            "type": params["order_type"],
            "quantity": params["quantity"]
        }

        if params["order_type"] == "LIMIT":
            order_args["price"] = str(params["price"])
            order_args["timeInForce"] = "GTC"  

        response = client.futures_create_order(**order_args)
        
        logger.info(f"API order placement successful. Raw Response: {response}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error encountered: Code={e.code}, Message={e.message}")
        raise e
    except BinanceRequestException as e:
        logger.error(f"Network / Request Failure while contacting Binance: {e}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected internal failure: {str(e)}")
        raise e