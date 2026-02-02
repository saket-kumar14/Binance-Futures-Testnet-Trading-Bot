from bot.logging_config import setup_logging
import logging
from bot.client import get_client
import argparse
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price
import time


# setup_logging()

# client = get_client()
# bal = client.futures_account_balance()

# # print("Futures Account Balance:", balance)
# # print("Type:", type(balance))


# usdt = next(
#     (item for item in bal if item["asset"] == "USDT"),
#     None
# )
# print("USDT Balance:", usdt["balance"])

def main():
    setup_logging()
    logger = logging.getLogger("cli")

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n=== Order Request Summary ===")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")
        print("=============================\n")

        client = get_client()

        response = place_order(
            client,
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        time.sleep(1)

        print("========Order Placed Successfully:========\n")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Quantity: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")
        print("==========================================\n")

    except Exception as e:
        logger.error(f"Error placing order: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

