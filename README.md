# OptionForge

A professional Python quantitative options analytics framework.

OptionForge is a modular options analytics engine designed for quantitative research, options pricing, implied volatility analysis, Greeks, option chain analytics, and future market intelligence.

---

# Current Version

**OptionForge Foundation v0.1**

Status:

- Stable
- Fully Tested
- Modular Architecture

---

# Features

## Quantitative Engine

- Black-Scholes Pricing
- Implied Volatility Solver
- Greeks
    - Delta
    - Gamma
    - Theta
    - Vega
- Root Solver
- Normal Distribution

---

## Analytics

- Option Analytics
- Option Chain Analytics

---

## Models

- OptionContract
- AnalyticsResult
- MarketSnapshot

---

## Storage

- Parquet Writer
- Parquet Reader
- Schema Management

---

## Utilities

- Data Loader
- Data Validator
- Date Utilities

---

## Validation

- Broker Comparison
- Accuracy Validation

---

## Testing

Complete automated test suite.

```
python run_tests.py
```

Current Status

```
12 Tests Passed
0 Tests Failed
```

---

# Project Structure

```
OptionForge

├── optionforge
│
│   ├── analytics
│   ├── config
│   ├── models
│   ├── profiles
│   ├── quant
│   ├── research
│   ├── storage
│   ├── utils
│   └── validation
│
├── tests
│
│   ├── analytics
│   ├── core
│   ├── integration
│   ├── models
│   ├── storage
│   └── validation
│
├── examples
├── output
├── data
│
├── run_tests.py
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

# Installation

Clone the repository

```bash
git clone <repository>
```

Go to project

```bash
cd OptionForge
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run complete framework validation

```bash
python run_tests.py
```

---

# Example

```python
from optionforge.quant.black_scholes import BlackScholes

price = BlackScholes.call_price(
    spot=25000,
    strike=25000,
    time=30/365,
    rate=0.06,
    volatility=0.20,
)

print(price)
```

---

# Design Philosophy

OptionForge follows a layered architecture.

```
Mathematics
        │
        ▼
Quantitative Engine
        │
        ▼
Analytics
        │
        ▼
Profiles
        │
        ▼
Research
        │
        ▼
Market Intelligence
```

Each layer has a single responsibility and is independently testable.

---

# Development Roadmap

## Foundation (Completed)

- Black-Scholes
- Greeks
- Implied Volatility
- Root Solver
- Option Analytics
- Option Chain
- Storage
- Validation
- Automated Test Suite

---

## Intelligence (Planned)

- Expected Move
- IV Rank
- IV Percentile
- OI Profile
- Gamma Profile
- Volume Profile
- Dealer Positioning
- Volatility Surface

---

# Quality

Current Framework Status

```
Core Mathematics      PASS
Models                PASS
Analytics             PASS
Storage               PASS
Validation            PASS
Integration           PASS

Total Tests

12 Passed
0 Failed
```

---

# License

Private Project

Copyright © 2026 OptionForge

All Rights Reserved.
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
OptionForge

Professional Quantitative Options Analytics Framework

✓ Black-Scholes Pricing

✓ Greeks

✓ Implied Volatility

✓ Option Chain Analytics

✓ Expected Move

✓ IV Rank

✓ IV Percentile

✓ Max Pain

✓ OI Wall

✓ OI Change

✓ OI Shift

✓ Support Strength

✓ Resistance Strength

✓ Market Structure

✓ Probability Engine

✓ Strategy Engine

Market Data

↓

Quant Engine

↓

Analytics

↓

Intelligence

↓

Market Structure

↓

Probability

↓

Strategy
Current Release

v0.6.0