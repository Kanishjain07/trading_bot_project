from config import API_KEY, API_SECRET
from bot import BasicBot
from logger import setup_logger

def main():
    # Setup logger
    logger = setup_logger()
    logger.info("Starting Trading Bot CLI")

    # Create bot instance
    bot = BasicBot(API_KEY, API_SECRET, testnet=True, logger=logger)

    print("=== Welcome to the Binance Futures Trading Bot ===")
    print("Note: This works only on the Binance Futures Testnet.\n")

    # Get user input
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (buy/sell): ").strip().lower()
    order_type = input("Enter order type (MARKET or LIMIT): ").strip().upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = input("Enter limit price: ")

    print("\nPlacing your order...\n")
    result = bot.place_order(symbol, side, order_type, quantity, price)

    if "error" in result:
        print("❌ Order failed:", result["error"])
    else:
        print("✅ Order placed successfully!")
        print("Order Details:")
        print(result)

if __name__ == "__main__":
    main()
