# OptionForge

> **Professional Quantitative Options Research Platform**

> **Let's build it right.**

---

# Overview

OptionForge is a professional, modular, and research-driven quantitative options platform designed for serious options traders, quantitative researchers, software engineers, and financial analysts.

Unlike traditional options libraries that focus only on pricing models or isolated indicators, OptionForge models the options market using real financial concepts and transforms raw market data into structured intelligence.

Every component is designed around software engineering principles, financial correctness, mathematical accuracy, and long-term maintainability.

OptionForge is built to become a platform—not a collection of scripts.

---

# Vision

To build a world-class quantitative options research platform that remains correct, maintainable, explainable, and extensible for years.

The objective is not to create the largest options library.

The objective is to create one of the most trusted options engineering platforms.

---

# Mission

OptionForge exists to bridge three disciplines into one unified framework.

- Quantitative Finance
- Software Engineering
- Market Research

Every calculation, every engine, every module, and every research model must satisfy all three disciplines.

---

# Philosophy

OptionForge follows one simple philosophy.

> **Build it right.**

This philosophy influences every engineering decision.

Correctness is preferred over shortcuts.

Readability is preferred over clever code.

Engineering discipline is preferred over rapid feature development.

The project is designed for long-term evolution rather than short-term development.

---

# Why OptionForge?

Most options projects begin as independent scripts.

Over time they become difficult to understand.

Calculations become duplicated.

Business logic becomes scattered.

Testing becomes difficult.

Maintenance becomes expensive.

OptionForge solves these problems by creating a professional engineering framework where every financial concept has one responsibility and every calculation has one home.

Instead of disconnected scripts, OptionForge provides a complete quantitative ecosystem.

---

# Core Principles

OptionForge is built around the following permanent principles.

## 1. Build it right.

Never sacrifice correctness for speed.

---

## 2. Financial truth before software convenience.

Software must represent the financial market correctly.

The market never changes because software is easier.

---

## 3. One responsibility per module.

Every module has exactly one reason to exist.

---

## 4. One owner per financial concept.

Every important financial concept belongs to exactly one object.

No duplication.

---

## 5. Research before assumptions.

Every important engineering decision should be supported by evidence.

---

## 6. Tests before trust.

If it cannot be tested,
it cannot be trusted.

---

## 7. Documentation is part of the product.

Documentation is never considered optional.

---

## 8. Simplicity beats unnecessary complexity.

If two solutions solve the same problem equally well,

the simpler solution wins.

---

# Engineering Principles

OptionForge follows professional software engineering standards.

- Domain Driven Design
- Clean Architecture
- Test Driven Development
- Modular Design
- Strong Typing
- Explicit APIs
- Immutable Domain Objects where appropriate
- Reusable Components
- Small Pull Requests
- Professional Git Workflow

---

# Design Goals

The platform is designed to be

- Correct
- Stable
- Modular
- Reusable
- Testable
- Explainable
- Extensible
- Maintainable

These qualities are considered more important than the total number of implemented features.

---

# What OptionForge Is

OptionForge is

- a quantitative research platform
- a professional Python library
- an options analytics framework
- a reusable engineering toolkit
- a financial domain model
- a research environment

---

# What OptionForge Is NOT

OptionForge is not

- a trading bot
- a signal selling platform
- a collection of indicators
- a copy of existing options libraries
- a dashboard-only project

Its purpose is to provide trusted financial infrastructure for quantitative research.

---

# Architecture Philosophy

The architecture models the financial market rather than software convenience.

Every major object represents a real financial entity.

The project separates

- Domain Model
- Analytics
- Research
- Infrastructure
- Visualization

This separation allows every layer to evolve independently while maintaining a stable foundation.

---

# Core Domain Model

The entire platform is built on the following financial hierarchy.

```text
TradingSession
        │
        ▼
Symbol
        │
        ▼
Expiry
        │
        ▼
Strike
        │
        ▼
Contract
        │
        ▼
Analytics
        │
        ▼
Research
        │
        ▼
Decision Engine
```

Every layer builds upon the layer beneath it.

No layer bypasses the domain model.

---

# Engineering Constitution

Every Pull Request must satisfy the following requirements.

✅ Financially Correct

✅ Mathematically Correct

✅ Type Safe

✅ Tested

✅ Documented

✅ Maintainable

✅ Review Ready

Only then is a Pull Request considered complete.

---

# Repository Structure

```text
OptionForge/

├── docs/
│
├── examples/
│
├── optionforge/
│   │
│   ├── common/
│   ├── kernel/
│   ├── analytics/
│   ├── research/
│   ├── downloader/
│   ├── storage/
│   ├── visualization/
│   └── utils/
│
├── tests/
│
├── README.md
├── pyproject.toml
├── LICENSE
├── CHANGELOG.md
└── .gitignore
```

---

# Package Overview

The project is divided into several logical layers.

### common

Shared constants, enumerations, exceptions, helper utilities, validation rules, and reusable infrastructure.

---

### kernel

Core financial domain objects.

Examples include

- TradingSession
- Symbol
- Expiry
- Strike
- Contract

These classes represent the financial language of OptionForge.

---

### analytics

Deterministic quantitative calculations.

Examples include

- Black-Scholes
- Greeks
- Implied Volatility
- Probability
- Expected Move
### research

The research layer contains experimental and validated quantitative research.

Examples include

- Modified PCR
- Dealer Position
- OI Migration
- Market Memory
- Volatility Regime
- Smart Money Models
- AI Ranking Models

Research modules are separated from production analytics until they are fully validated.

---

### downloader

Responsible for collecting market data from supported data providers.

Responsibilities include

- Historical Data
- Live Market Data
- Option Chain Data
- Future Data
- Session Management

---

### storage

Provides a unified persistence layer.

Supported storage formats include

- CSV
- Parquet
- SQLite
- Future Database Integration

---

### visualization

Professional dashboards, reports, charts, and market visualization.

Visualization never performs financial calculations.

It only presents already validated results.

---

### tests

Contains the complete automated testing suite.

Every production module must include unit tests.

No feature is considered complete without passing tests.

---

# Feature Roadmap

OptionForge is developed in logical layers.

## Foundation

- Trading Session
- Symbol
- Expiry
- Strike
- Contract
- Domain Validation

---

## Quantitative Mathematics

- Black-Scholes
- Greeks
- Implied Volatility
- Root Solver
- Normal Distribution
- Probability Models

---

## Market Analytics

- Option Chain Analytics
- Open Interest Analytics
- OI Change
- OI Shift
- PCR
- Modified PCR
- Max Pain
- Support Strength
- Resistance Strength
- Expected Move
- IV Rank
- IV Percentile
- Volatility Surface

---

## Market Intelligence

- Dealer Position
- Gamma Exposure
- Delta Exposure
- Market Structure
- Volatility Regime
- Liquidity Analysis
- Smart Money Detection

---

## Decision Engine

The Decision Engine combines multiple analytics into explainable outputs.

Every signal should answer

- What happened?
- Why?
- Confidence?
- Supporting Evidence?
- Risk?

Signals should never be black boxes.

---

## Professional Applications

- Dashboard
- Scanner
- Professional Reports
- Daily Workflow
- Research Notebook
- Strategy Evaluation

---

# Installation

Clone the repository

```bash
git clone https://github.com/harshlearn001/OptionForge.git
```

Move into the project

```bash
cd OptionForge
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Quick Start

Example

```python
from optionforge.analytics.black_scholes import BlackScholes

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

# Development Workflow

Every feature follows the same engineering process.

```text
Research
      │
      ▼
Design
      │
      ▼
Implementation
      │
      ▼
Unit Tests
      │
      ▼
Code Review
      │
      ▼
Git Commit
      │
      ▼
Merge
```

No step should be skipped.

---

# Testing Philosophy

Testing is considered part of development.

Every important module should include

- Happy Path Tests
- Boundary Tests
- Invalid Input Tests
- Serialization Tests
- Regression Tests

If it cannot be tested,

it cannot be trusted.

---

# Documentation Philosophy

Every major module should explain

- Purpose
- Financial Theory
- Mathematical Model
- Implementation
- Examples
- Limitations

Documentation is considered a production asset.

---

# Contributing

Future contributors should follow these principles.

- Build it right.
- Keep modules focused.
- Write readable code.
- Add tests.
- Update documentation.
- Keep Pull Requests small.
- Respect the domain model.

---

# Versioning

OptionForge follows Semantic Versioning.

```text
MAJOR.MINOR.PATCH
```

Example

```text
1.2.0
```

- MAJOR → Breaking Changes
- MINOR → New Features
- PATCH → Bug Fixes

---

# Roadmap

Planned milestones

- Foundation Layer
- Quantitative Mathematics
- Market Intelligence
- Research Platform
- Decision Engine
- Professional Dashboard
- Historical Database
- Backtesting Framework
- OptionForge v1.0

The roadmap evolves through validated engineering decisions rather than feature accumulation.

---

# Engineering Philosophy

OptionForge follows one permanent philosophy.

> Build it right.

That means

- correctness before speed
- simplicity before complexity
- evidence before assumptions
- research before implementation
- tests before trust

The objective is not to write more code.

The objective is to write better software.

---

# Current Status

| Item | Status |
|------|--------|
| Architecture | Locked |
| Engineering Standards | Established |
| Domain Model | Complete |
| Development | Active |
| Testing Philosophy | Defined |
| Documentation | Active |

---

# License

Private Project

Copyright © 2026 OptionForge

All Rights Reserved.

---

# Founder Quote

> "Great software is not built by writing the most code.
>
> Great software is built by making thousands of small, correct engineering decisions."

---

# Motto

> **Let's build it right.**
