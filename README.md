# 🧠 Simplified Binance Futures Trading Bot

A Python-based command-line bot that interacts with the **Binance Futures Testnet** using the official `python-binance` library. It supports **market** and **limit** orders for **buy/sell** actions. Designed to demonstrate real-world API usage, automation, and structured coding skills.

---

## ✅ Features

- Market & Limit order support  
- Buy/Sell functionality  
- Binance Futures Testnet integration  
- Command-Line Interface (CLI)  
- Logging of API requests, responses, and errors  
- Modular and beginner-friendly code  

---

## 📁 Project Structure
trading_bot_project/
├── bot.py # Main trading logic (API interaction)
├── main.py # CLI interface for user input/output
├── config.py # API keys and testnet configuration
├── logger.py # Logging setup
├── requirements.txt
## 🔧 How to Use

1. Sign up at [https://testnet.binancefuture.com](https://testnet.binancefuture.com)  
2. Generate your API Key and Secret  
3. Paste them into `config.py`:

```python
API_KEY = "your_api_key"
API_SECRET = "your_secret_key"
BASE_URL = "https://testnet.binancefuture.com"
2. Install Dependencies
pip install -r requirements.txt

3. Set Up API Keys
Create a Binance Futures Testnet account: https://testnet.binancefuture.com
Paste your API credentials into config.py:
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
BASE_URL = "https://testnet.binancefuture.com"
'''
🖥️ Running the Bot
python main.py

🛠 Tech Stack
Python 3.x

python-binance

Binance Futures Testnet

Logging module

🙋 Author
Kanish Jain
Built as part of a hiring challenge to demonstrate API handling and automation skills with real-world tools.
