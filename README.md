# OptionForge

> **Professional Quantitative Options Intelligence Framework**

OptionForge is a modular, test-driven Python framework for quantitative options analysis.

It transforms raw option-chain data into structured analytics, market intelligence, probability estimation, strategy generation, dashboards, reports, and market scanners through a clean, reusable architecture.

---

# Vision

OptionForge is designed to be a long-term quantitative engineering framework rather than a collection of standalone scripts.

The project emphasizes:

* Modular Architecture
* Test-Driven Development
* Reusable Components
* Clean Engineering
* Stable Releases
* Maintainable Code

Every module has a single responsibility and integrates into a unified analysis pipeline.

---

# Why OptionForge?

Many options projects begin as independent scripts.

As they grow, calculations become duplicated, testing becomes difficult, and maintenance becomes increasingly complex.

OptionForge solves this problem by providing a structured framework where every component is reusable and professionally organized.

Instead of isolated scripts, OptionForge provides:

* Quantitative Pricing
* Volatility Intelligence
* Open Interest Intelligence
* Market Structure Analysis
* Probability Estimation
* Strategy Generation
* Professional Reports
* Dashboard Generation
* Market Scanning
* Extensible Data Loading

The goal is simple:

> **Build a framework that remains clean, testable, and maintainable for years.**

---

# Features

## Quantitative Engine

* Black-Scholes Pricing
* Greeks

  * Delta
  * Gamma
  * Theta
  * Vega
* Implied Volatility Solver
* Root Solver
* Normal Distribution

---

## Analytics

* Option Analytics
* Option Chain Analytics
* Market Snapshot

---

## Market Intelligence

* Expected Move
* IV Rank
* IV Percentile
* Max Pain
* OI Wall
* OI Change
* OI Shift
* Support Strength
* Resistance Strength
* Market Structure
* Probability Engine
* Strategy Engine

---

## Applications

* Professional Report Engine
* Professional Dashboard
* Professional Market Scanner

---

## Data

* Market Data Loader
* Storage Layer
* Validation Framework

---

# Architecture

```text
Market Data
      │
      ▼
Analytics
      │
      ▼
Intelligence
      │
      ▼
Market Structure
      │
      ▼
Probability
      │
      ▼
Strategy
      │
      ▼
Scanner
      │
      ▼
Dashboard
      │
      ▼
Reports
```

---

# Project Structure

```text
OptionForge/

├── optionforge/
│   ├── analytics/
│   ├── dashboard/
│   ├── datasource/
│   ├── intelligence/
│   ├── models/
│   ├── quant/
│   ├── reports/
│   ├── storage/
│   └── utils/
│
├── tests/
│
├── README.md
├── pyproject.toml
├── requirements.txt
├── run_tests.py
└── optionforge_scanner.py
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/harshlearn001/OptionForge.git
```

Enter the project directory

```bash
cd OptionForge
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Test Suite

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
    time=30 / 365,
    rate=0.06,
    volatility=0.20,
)

print(price)
```

---

# Professional Workflow

```text
Market Data

↓

Analytics

↓

Intelligence

↓

Probability

↓

Strategy

↓

Scanner

↓

Dashboard

↓

Report
```

---

# Current Status

| Item               | Status           |
| ------------------ | ---------------- |
| Current Version    | **v0.9.0**       |
| Professional Tests | **28 / 28 PASS** |
| Repository         | Stable           |
| Architecture       | Modular          |
| Development        | Active           |

---

# Release History

| Version | Major Milestone                |
| ------- | ------------------------------ |
| v0.1.0  | Core Quant Engine              |
| v0.2.0  | Volatility Intelligence        |
| v0.3.0  | Professional OI Intelligence   |
| v0.4.0  | Market Strength                |
| v0.5.0  | Market Structure & Probability |
| v0.6.0  | Strategy Engine                |
| v0.7.0  | Professional Report Engine     |
| v0.8.0  | Professional Dashboard         |
| v0.9.0  | Professional Market Scanner    |

---

# Roadmap

Upcoming milestones include:

* Real Market Data Integration
* Daily Workflow Engine
* Historical Database Support
* Backtesting Framework
* OptionForge v1.0

---

# Engineering Philosophy

OptionForge follows these principles:

* One Responsibility per Module
* Reusable Components
* Structured Data Models
* Test-Driven Development
* Stable Versioned Releases
* Professional Git Workflow

> **Build for years, not for today.**

---

# License

Private Project

Copyright © 2026 OptionForge

All Rights Reserved.
