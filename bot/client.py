import os
import logging
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("trading_bot")

def get_binance_client():
    """Initializes and returns the Binance client configured explicitly for Futures Testnet."""
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        logger.error("Missing BINANCE_API_KEY or BINANCE_API_SECRET in environment variables.")
        raise ValueError("API credentials missing. Please set them in your environment or .env file.")
        
    client = Client(
        api_key, 
        api_secret, 
        requests_params={"timeout": 10}
    )

    client.API_URL = 'https://testnet.binance.vision/api'  
    client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi' 
    
    return client