from binance.client import Client
from binance.enums import *

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True, logger=None):
        """
        Initialize the Binance Futures client.
        """
        self.logger = logger
        self.client = Client(api_key, api_secret)

        # Connect to Binance Testnet if testnet=True
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"
            if self.logger:
                self.logger.info("Connected to Binance Futures Testnet")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Place a futures order on Binance (Market or Limit).

        Parameters:
        - symbol: e.g. 'BTCUSDT'
        - side: 'buy' or 'sell'
        - order_type: 'MARKET' or 'LIMIT'
        - quantity: amount to buy/sell
        - price: required only for LIMIT order
        """
        try:
            # Set the order parameters
            order_data = {
                "symbol": symbol,
                "side": SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                "type": order_type.upper(),
                "quantity": quantity
            }

            # Add price and timeInForce if it's a LIMIT order
            if order_type.upper() == ORDER_TYPE_LIMIT:
                order_data["price"] = price
                order_data["timeInForce"] = TIME_IN_FORCE_GTC

            # Logging
            if self.logger:
                self.logger.info(f"Placing order: {order_data}")

            # Create the order
            response = self.client.futures_create_order(**order_data)

            if self.logger:
                self.logger.info(f"Order successful: {response}")
            return response

        except Exception as e:
            error_message = f"Order failed: {str(e)}"
            if self.logger:
                self.logger.error(error_message)
            return {"error": error_message}
