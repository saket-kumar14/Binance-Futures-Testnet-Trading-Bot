# Binance-Futures-Testnet-Trading-Bot



## Clone From GitHub

```bash
git clone https://github.com/<your-username>/Binance-Futures-Testnet-Trading-Bot.git
cd Binance-Futures-Testnet-Trading-Bot
```

---

## Testnet Setup

1. Create Binance Futures Testnet account

2. Generate API keys

---

## Create Virtual Environment

Linux / Mac:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Set Environment Variables

Linux / Mac:

```bash
export BINANCE_API_KEY=your_api_key
export BINANCE_API_SECRET=your_api_secret
```

Windows (cmd):

```bash
set BINANCE_API_KEY=your_api_key
set BINANCE_API_SECRET=your_api_secret
```

---

## Run

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

---

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000
```

---

## CLI Parameters

```
--symbol     Trading pair (example: BTCUSDT)
--side       BUY or SELL
--type       MARKET or LIMIT
--quantity   Order quantity
--price      Required only for LIMIT orders
```

---


## Logs

Logs are written to logs/trading_bot.log
