# Secure Code Review Tool

## CodSoft Cyber Security Internship - Task 3

A Python-based static security code review tool that analyzes source code and identifies common security weaknesses.

## Project Overview

This project demonstrates basic static code analysis using Python's Abstract Syntax Tree (AST) module.

The scanner analyzes a sample Python application containing intentionally introduced security weaknesses and generates a security review report.

## Files

- `vulnerable_app.py` - Sample application containing intentional security weaknesses.
- `security_scanner.py` - Static security analyzer.
- `README.md` - Project documentation.

## Security Issues Detected

The scanner detects the following issues:

### 1. Hardcoded Passwords and Secrets

Hardcoded passwords and API keys can expose sensitive information if source code is shared or published.

**Recommendation:** Store secrets in environment variables or a secure secret manager.

### 2. eval() Usage

The `eval()` function can execute dynamically supplied Python expressions and may create serious security risks when used with untrusted input.

**Recommendation:** Avoid `eval()` and use safe parsing or restricted operations.

### 3. Unsafe User Input

Functions that accept potentially unsafe input should validate and sanitize that input before processing it.

**Recommendation:** Apply input validation and restrict accepted values.

### 4. os.system() Usage

Executing shell commands with potentially user-controlled input can introduce command execution vulnerabilities.

**Recommendation:** Avoid unsafe shell execution and use safer APIs with strict input validation.

## Security Scan Result

The scanner successfully identified:

- 2 hardcoded secrets
- 2 high-severity dangerous function usages
- 2 medium-severity unsafe input findings

**Total findings: 6**

## Technologies Used

- Python 3
- Python AST module
- Static Code Analysis

## How to Run

Open the project folder in a terminal:

```bash
python security_scanner.py