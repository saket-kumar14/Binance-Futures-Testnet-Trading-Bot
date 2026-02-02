import logging


logger = logging.getLogger(__name__)


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(
            f"Placing {order_type} order for {quantity} {symbol} at price {price} with side {side}"
            )
        
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
        
        logger.info(f"Order placed successfully: {order}")
        return order
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise

