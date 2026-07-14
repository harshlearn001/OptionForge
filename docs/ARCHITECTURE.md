# OptionForge Architecture

## Overview

OptionForge is an institutional-grade options research platform built
around a layered architecture.

Each layer has a single responsibility and communicates only with the
layer immediately above or below it.

This design provides:

- Modular development
- Testability
- Maintainability
- Reusability
- Clear separation of concerns

---

# High-Level Architecture

                    OptionForge

          ┌─────────────────────┐
          │     Repository       │
          └─────────┬───────────┘
                    │
          ┌─────────▼───────────┐
          │      Providers      │
          └─────────┬───────────┘
                    │
          ┌─────────▼───────────┐
          │ Snapshot Builder    │
          └─────────┬───────────┘
                    │
          ┌─────────▼───────────┐
          │ Analytics Engine    │
          └─────────┬───────────┘
                    │
          ┌─────────▼───────────┐
          │ Knowledge Engine    │
          └─────────┬───────────┘
                    │
          ┌─────────▼───────────┐
          │ Decision Engine     │
          └─────────┬───────────┘
                    │
          ┌─────────▼───────────┐
          │ Strategy Engine     │
          └─────────┬───────────┘
                    │
          ┌─────────▼───────────┐
          │ Portfolio Engine    │
          └─────────┬───────────┘
                    │
          ┌─────────▼───────────┐
          │ Execution Engine    │
          └─────────────────────┘

---

# Layer Responsibilities

## Repository

Responsible for loading market data.

Examples

- Spot Data
- Futures
- Option Chain
- Risk-Free Rates

---

## Providers

Convert raw market data into reusable features.

Examples

- IV Rank Provider
- Expected Move Provider
- Gamma Exposure Provider
- Dealer Position Provider

---

## Snapshot

Creates immutable market snapshots.

Every analytics engine consumes snapshots rather than raw data.

---

## Analytics

Performs quantitative calculations.

Includes:

- Greeks
- Implied Volatility
- IV Rank
- IV Percentile
- Expected Move
- Gamma Exposure
- Volatility Smile
- Volatility Surface
- PCR
- Max Pain
- Dealer Position

---

## Knowledge

Transforms analytics into market intelligence.

Examples:

- Dealer positioning
- Volatility regime
- Risk state
- Market bias

---

## Decision

Combines evidence into actionable decisions.

Examples:

- Buy
- Sell
- Hold
- Neutral

---

## Strategy

Creates trading strategies from decisions.

---

## Portfolio

Portfolio construction and capital allocation.

---

## Execution

Execution planning and trade management.

---

# Design Principles

OptionForge follows:

- Layered Architecture
- Single Responsibility Principle
- Composition over Inheritance
- Immutable Result Objects
- Test-Driven Development
- Strong Typing

---

# Testing

Current regression suite:

1665 automated tests

All passing.

---

# Version

Current stable branch:

v0.9.9

Preparing:

v1.0.0