import os
import logging
from binance.client import Client

logger = logging.getLogger(__name__)

BASE_URL = "https://testnet.binancefuture.com"

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    # print("API:", api_key)
    # print("SECRET:", secret_key)

    if not api_key or not secret_key:
        raise ValueError("API credentials does not match")
    

    client = Client(api_key, secret_key, testnet=True)
    client.FUTURES_URL = BASE_URL

    logger.info("Testnet Initiated")

    return client