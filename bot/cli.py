import questionary
import sys
from bot.logging_config import setup_logging
from bot.validators import validate_inputs
from bot.client import get_binance_client
from bot.orders import place_futures_order

# Initialize logging structure
logger = setup_logging()

def main():
    print("\n=============================================")
    print("🤖  Interactive Binance Futures Trading Bot  🤖")
    print("=============================================\n")

    try:
        # 1. Interactive Menu for Symbol with default selection
        symbol = questionary.text(
            "Enter Trading Pair Asset (e.g., BTCUSDT):",
            default="BTCUSDT"
        ).ask()
        
        if not symbol:
            print("❌ Execution cancelled. Symbol cannot be empty.")
            return

        # 2. Dropdown choice menu for Side selection
        side = questionary.select(
            "Select Order Direction (Side):",
            choices=["BUY", "SELL"]
        ).ask()

        # 3. Dropdown choice menu for Order Type selection
        order_type = questionary.select(
            "Select Order Type Format:",
            choices=["MARKET", "LIMIT"]
        ).ask()

        # 4. Interactive text input with real-time positive number validation
        quantity_str = questionary.text(
            "Enter Asset Volume Quantity:",
            validate=lambda text: True if text.replace('.', '', 1).isdigit() and float(text) > 0 
            else "Quantity must be a positive number greater than 0."
        ).ask()
        quantity = float(quantity_str)

        # 5. Conditional input: Only prompts for Price if a LIMIT order is chosen
        price = None
        if order_type == "LIMIT":
            price_str = questionary.text(
                "Enter Limit Unit Price (USDT):",
                validate=lambda text: True if text.replace('.', '', 1).isdigit() and float(text) > 0 
                else "Price must be a positive number greater than 0 for LIMIT orders."
            ).ask()
            price = float(price_str)

        # Run your clean verification processing engine 
        valid_params = validate_inputs(symbol, side, order_type, quantity, price)
        
        # Render clean request overview layout on console screen
        print("\n=== [ORDER REQUEST SUMMARY] ===")
        print(f"Symbol   : {valid_params['symbol']}")
        print(f"Side     : {valid_params['side']}")
        print(f"Type     : {valid_params['order_type']}")
        print(f"Quantity : {valid_params['quantity']}")
        if valid_params['price']:
            print(f"Price    : {valid_params['price']}")
        print("===============================\n")

        print("⏳ Connecting to Binance Futures Testnet...")
        client = get_binance_client()

        print("🚀 Executing trade order call transaction...")
        response = place_futures_order(client, valid_params)

        # Parse structural data mappings out from server response dictionary payload
        order_id = response.get("orderId")
        status = response.get("status")
        exec_qty = response.get("executedQty", 0)
        avg_price = response.get("avgPrice", "N/A")

        # Success message with color-emulated text blocks
        print("\n🟢 ORDER PLACED SUCCESSFULLY!")
        print(f"OrderID      : {order_id}")
        print(f"Status       : {status}")
        print(f"Executed Qty : {exec_qty}")
        print(f"Avg Price    : {avg_price}\n")

    except Exception as err:
        print("\n🔴 ORDER FAILED!")
        print(f"Error Details: {str(err)}\n")

if __name__ == "__main__":
    main()