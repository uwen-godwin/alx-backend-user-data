#!/usr/bin/env python3
"""
Main script to choose between logging and password encryption functionalities.
"""

import logging
import bcrypt
import getpass
import os

# Logging setup
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def filter_logs(file_path: str, level: str):
    """
    Filters log entries based on the specified logging
    level and writes them to a new file.

    Args:
        file_path (str): Path to the log file.
        level (str): Logging level to filter by (e.g., INFO, WARNING).
    """
    level = level.upper()
    levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    if level not in levels:
        print(f"Invalid level: {level}")
        return

    with open(file_path, 'r') as infile, open(f"filtered_{level.lower()}.log", 'w') as outfile:
        for line in infile:
            if level in line:
                outfile.write(line)

    print(f"Filtered logs have been saved to filtered_{level.lower()}.log")


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a salt.

    Args:
        password (str): Password to hash.

    Returns:
        bytes: Hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to check.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)


def encrypt_password():
    """
    Prompts the user to enter a password,
    hashes it, and displays the hashed password.
    """
    password = getpass.getpass(prompt="Enter a password to encrypt: ")
    hashed = hash_password(password)
    print(f"Encrypted password: {hashed.decode()}")


def verify_password():
    """
    Prompts the user to enter a password and
    verify it against a stored hashed password.
    """
    hashed_password = getpass.getpass(prompt="Enter the hashed password: ")
    password = getpass.getpass(prompt="Enter the password to verify: ")

    # Convert the hashed password from string to bytes
    hashed_password_bytes = hashed_password.encode()

    if is_valid(hashed_password_bytes, password):
        print("Password is valid.")
    else:
        print("Password is invalid.")


def main():
    """
    Main function to prompt user for action and
    execute the corresponding functionality.
    """
    choice = input(
        "Choose an action (filter_logs/encrypt_password/verify_password): "
    ).strip().lower()

    if choice == 'filter_logs':
        file_path = input("Enter the path to the log file: ").strip()
        level = input(
            "Enter the logging level to filterby(DEBUG, INFO, WARNING, ERROR, CRITICAL): "
        ).strip()
        filter_logs(file_path, level)
    elif choice == 'encrypt_password':
        encrypt_password()
    elif choice == 'verify_password':
        verify_password()
    else:
        print(
            "Invalid choice. Please select 'filter_logs',
            'encrypt_password', or 'verify_password'."
        )


if __name__ == "__main__":
    main()
