# Interactive Binance Futures Trading Bot CLI

A modular, interactive Command Line Interface (CLI) application built in Python for executing trading orders seamlessly on the **Binance Futures Testnet (USDT-M)**. Upgraded with an advanced, interactive text UX that guides users dynamically with menu selectors and built-in entry validation.

## ✨ Core Features
* **Enhanced Interactive CLI UX:** Built using `questionary` to replace tedious flags with beautiful, interactive arrow-key select menus and live text prompts.
* **Modular Architecture:** Explicit separation of concerns between logging configurations, API clients, parameters validation, and execution code.
* **Robust Input Validation:** Intercepts out-of-bounds or formatting typing errors natively before sending live network calls.
* **Dual-Channel Structured Logging:** Automatically writes detailed execution records tracking exact script file names and lines concurrently to the console and a persistent local `trading_bot.log` file.
* **Production Exception Filters:** Safely isolates and maps network connection loss (`BinanceRequestException`) distinct from internal account verification/margin rule drops (`BinanceAPIException`).

---

## 📂 Project Architecture

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── cli.py             # Interactive execution layer (Entry Point)
│   ├── client.py          # Binance API initialization module 
│   ├── logging_config.py  # Dual Console/FileHandler logger setup
│   ├── orders.py          # Futures trade parameters router mapping 
│   └── validators.py      # Entry filters and business rule parameters check
│
├── .env                   # Local system environment variables (Ignored in git)
├── .gitignore             # Safety rules ensuring credentials stay hidden
├── requirements.txt       # Project direct dependencies inventory manifest
├── trading_bot.log        # Automatically generated audit trail ledger (Deliverable)
└── README.md              # Documentation manual handbook
```


🚀 Getting Started
1. Prerequisites & Installation
Ensure you have Python 3.8+ installed. Initialize your environment and install packages using the terminal:

```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate

# Install required library dependencies
pip install -r requirements.txt
```

2. Configure Environment Keys
Create a file named .env inside your root project folder and supply your Binance Futures Testnet API credentials:

```
BINANCE_API_KEY=your_actual_testnet_api_key_here
BINANCE_API_SECRET=your_actual_testnet_api_secret_here
```

3. Execution Tutorial
Launch the fully automated interactive loop with a single terminal instruction:

```
python -m bot.cli
```

📈 Audit Ledger Records (trading_bot.log)
The bot tracks and commits every event directly to trading_bot.log. Here is an overview example showing both structural API validations catching rule mismatches and a finalized active execution record:

```
2026-07-06 11:45:51,615 - INFO - [orders.py:9] - Sending API request to Binance Testnet with params: {'symbol': 'BTCUSDT', 'side': 'BUY', 'order_type': 'LIMIT', 'quantity': 1.25, 'price': 5.69}
2026-07-06 11:45:52,522 - ERROR - [orders.py:28] - Binance API Error encountered: Code=-4013, Message=Price less than min price.

2026-07-06 11:49:23,691 - INFO - [orders.py:9] - Sending API request to Binance Testnet with params: {'symbol': 'BTCUSDT', 'side': 'SELL', 'order_type': 'LIMIT', 'quantity': 2.36, 'price': 60000.0}
2026-07-06 11:49:24,517 - ERROR - [orders.py:28] - Binance API Error encountered: Code=-2019, Message=Margin is insufficient.

2026-07-06 11:55:56,703 - INFO - [orders.py:9] - Sending API request to Binance Testnet with params: {'symbol': 'ETHUSDT', 'side': 'BUY', 'order_type': 'MARKET', 'quantity': 1.24, 'price': None}
2026-07-06 11:55:57,332 - INFO - [orders.py:24] - API order placement successful. Raw Response: {'orderId': 12108518845, 'symbol': 'ETHUSDT', 'status': 'NEW', 'clientOrderId': 'Y1sXkoZs...', 'price': '0.00', 'origQty': '1.240', 'executedQty': '0.000', 'cumQty': '0.000', 'timeInForce': 'GTC', 'type': 'MARKET', 'reduceOnly': False, 'side': 'BUY', 'updateTime': 1783319157487}

```

