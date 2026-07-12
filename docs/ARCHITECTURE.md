# OptionForge Architecture

## Vision

OptionForge is an institutional-grade quantitative options research platform.

Primary goals:

- Historical options research
- Historical replay
- Signal generation
- Strategy research
- Feature engineering
- Machine learning
- Risk analytics

---

# Layer Architecture

Application

↓

Research

↓

Analytics

↓

Snapshot

↓

Provider

↓

Repository

↓

Integration

↓

Contracts

---

# Package Responsibilities

contracts/

Immutable schemas and interfaces.

No pandas.
No business logic.

---

integration/

Responsible for reading and validating data.

Contains:

- FileResolver
- MarketValidator
- MarketRepository

Never calculates analytics.

---

provider/

Provides market data.

Examples:

- nearest expiry
- option chain
- spot history
- futures history

---

snapshot/

Creates InstitutionalSnapshot objects.

No file reading.

No analytics.

---

analytics/

Calculations only.

Examples:

- PCR
- IV
- Greeks
- OI analytics
- Volatility
- VWAP
- Max Pain

Analytics never read files.

---

research/

Research engines.

Consumes InstitutionalSnapshot.

Produces research results.

---

storage/

Persistence.

Parquet

Cache

History

---

tests/

Mirror package structure.

Every production module has a matching test module.

---

# Dependency Rules

contracts

↓

integration

↓

repository

↓

provider

↓

snapshot

↓

analytics

↓

research

Dependencies only flow downward.

No circular imports.

---

# Coding Rules

- Type hints required.
- Public methods documented.
- Single Responsibility Principle.
- Prefer composition over inheritance.
- No hidden global state.
- Use custom exceptions.
- Avoid magic strings.
- Keep business logic out of repositories.

---

# Testing Rules

Every production module must have tests.

Required:

- import test
- success path
- failure path
- edge cases

No feature is complete until tests pass.

---

# Git Workflow

Write code

↓

Write tests

↓

pytest

↓

Commit

↓

Push

↓

Tag milestones

---

# Milestones

v0.1.0
Foundation ✅

v0.2.0
Repository

v0.3.0
Provider

v0.4.0
Snapshot

v0.5.0
Research

v1.0.0
OptionForge