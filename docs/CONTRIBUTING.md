# Contributing to OptionForge

First of all, thank you for your interest in contributing to OptionForge.

Our goal is to build a reliable, modular and well-tested options research platform.

---

# Development Philosophy

Every contribution should improve one or more of the following:

- Correctness
- Readability
- Maintainability
- Performance
- Test Coverage

---

# Coding Standards

## Python Version

Python 3.13+

---

## Style

- Follow PEP 8
- Use descriptive names
- Prefer composition over inheritance
- Keep functions focused on a single responsibility
- Use type hints where practical

---

# Testing

Every new feature should include tests.

Run the complete suite before submitting changes:

```bash
pytest
```

Expected result:

```
1665 passed
```

---

# Project Structure

OptionForge follows a layered architecture.

Repository

↓

Providers

↓

Snapshot

↓

Analytics

↓

Knowledge

↓

Decision

↓

Strategy

↓

Portfolio

↓

Execution

Each new module should fit naturally into one of these layers.

---

# Commit Messages

Use Conventional Commits.

Examples:

```
feat(analytics): add volatility skew engine

fix(repository): correct expiry parsing

test(greeks): improve calculator coverage

docs: update architecture
```

---

# Pull Requests

Please include:

- Clear description
- Related issue (if any)
- Tests
- Documentation updates (when applicable)

---

# Code Quality Checklist

Before submitting:

- Code builds
- Tests pass
- Type hints added where appropriate
- No unused imports
- No commented-out code
- Public APIs documented

---

Thank you for helping improve OptionForge.