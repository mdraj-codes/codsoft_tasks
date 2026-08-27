# Vulnerable Demo Application
# This file intentionally contains common security weaknesses
# for the purpose of security code review.

import os

USERNAME = "admin"
PASSWORD = "admin123"          # Hardcoded password
API_KEY = "12345-SECRET-KEY"   # Hardcoded secret


def login(username, password):
    if username == USERNAME and password == PASSWORD:
        return "Login successful"
    return "Invalid username or password"


def calculate(expression):
    # Dangerous: eval() can execute arbitrary Python code
    return eval(expression)


def run_command(command):
    # Dangerous: user-controlled command execution
    os.system(command)


def save_user_data(name):
    # No input validation
    print("Saving user:", name)


if __name__ == "__main__":
    print(login("admin", "admin123"))

    user_expression = input("Enter calculation: ")
    print("Result:", calculate(user_expression))

    user_name = input("Enter your name: ")
    save_user_data(user_name)