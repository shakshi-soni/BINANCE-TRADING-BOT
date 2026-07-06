# Interactive Binance Futures Trading Bot CLI

A modular, interactive Command Line Interface (CLI) application built in Python for executing trading orders seamlessly on the **Binance Futures Testnet (USDT-M)**. Upgraded with an advanced, interactive text UX that guides users dynamically with menu selectors and built-in entry validation.


# 🤖 Interactive Binance Futures Trading Bot CLI

## 🤔 What is this?
This project is an advanced, production-grade **Command Line Interface (CLI) Trading Assistant** designed specifically for the **Binance Futures Testnet (USDT-M)**. 

Instead of forcing users to deal with complex, error-prone terminal command flags (like `--symbol BTCUSDT --side BUY`), this application replaces the traditional CLI experience with a **dynamic, interactive terminal UX**. It uses visual select menus and real-time inputs to guide a trader step-by-step through configuring and sending a trade safely to the live exchange network.

Think of it as a bridge between complex crypto exchange rulebooks and a clean, bulletproof developer terminal tool.

## ✨ Core Features
* **Enhanced Interactive CLI UX:** Built using `questionary` to replace tedious flags with beautiful, interactive arrow-key select menus and live text prompts.
* **Modular Architecture:** Explicit separation of concerns between logging configurations, API clients, parameters validation, and execution code.
* **Robust Input Validation:** Intercepts out-of-bounds or formatting typing errors natively before sending live network calls.
* **Dual-Channel Structured Logging:** Automatically writes detailed execution records tracking exact script file names and lines concurrently to the console and a persistent local `trading_bot.log` file.
* **Production Exception Filters:** Safely isolates and maps network connection loss (`BinanceRequestException`) distinct from internal account verification/margin rule drops (`BinanceAPIException`).

---

## 🛠️ Technologies Used

The application is built completely using an industry-standard, lightweight, and highly asynchronous-capable Python ecosystem:

* **Python 3.8+**: The core execution programming language.
* **`questionary`**: Used to engineer the advanced, interactive terminal UX prompts, select menus, input captures, and keyboard arrow controls.
* **`python-binance`**: The official ecosystem REST API and WebSockets wrapper wrapper used to communicate securely with the Binance Futures Testnet endpoints.
* **`python-dotenv`**: Used to load environment-specific configurations and credentials from a detached `.env` profile securely into the system environment memory runtime (`os.environ`).
* **`logging` (Native Standard Library)**: Implements dual-stream pipeline handlers to pipe structured execution events onto both the terminal standard output stream (`stdout`) and local `trading_bot.log` append file ledgers simultaneously.

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

## 💡 Skills Demonstrated

Developing this application showcases several essential production-level software engineering capabilities:

* **Defensive Programming & Input Sanitization:** Implementing client-side pre-validation engines to ensure malicious or malformed data inputs are caught before consuming live network bandwidth or hitting external rate limits.
* **Structured Enterprise Logging:** Configuring dual-destination logging setups that preserve clean operational visibility for the user via terminal alerts while saving system debugging metadata (file names, modules, exact line numbers) to an audit log.
* **Graceful Exception Mapping:** Extracting deep, cryptic API errors from a live third-party network and translating them into helpful, human-readable terminal messages without leaking internal tracebacks.
* **Secure Environment Management:** Adhering strictly to information security practices by decoupling critical access keys and secrets using system environment abstraction (`.env` with strict `.gitignore` tracking).
* **Modular Software Design:** Organizing code into distinct files where logic is completely isolated (separation of concerns among execution triggers, input validation rules, and network calls).

---

## 🙋‍♂️ About the Developer

Built with ❤️ by **[SHAKSHI SONI]**

I'm a developer passionate about building practical AI applications that solve real-world problems. This project explores agentic AI design — where an LLM doesn't just chat, but *acts*, by calling tools, remembering context, and making decisions autonomously.
---

📫 **Connect with me:**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/yourprofile)


<div align="center">

**⭐ If you found this project interesting, please give it a star! It helps a lot.**

