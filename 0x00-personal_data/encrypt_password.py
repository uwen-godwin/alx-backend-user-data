#!/usr/bin/env python3
"""
Module to handle password encryption and verification.
"""

import bcrypt
import getpass
import os

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
    Prompts the user to enter a password, hashes it, and displays the hashed password.
    """
    password = getpass.getpass(prompt="Enter a password to encrypt: ")
    hashed = hash_password(password)
    print(f"Encrypted password: {hashed.decode()}")

def verify_password():
    """
    Prompts the user to enter a password and verify it against a stored hashed password.
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
    Main function to prompt user for action and execute the corresponding function.
    """
    choice = input("Choose an action (encrypt/verify): ").strip().lower()
    if choice == 'encrypt':
        encrypt_password()
    elif choice == 'verify':
        verify_password()
    else:
        print("Invalid choice. Please select 'encrypt' or 'verify'.")

if __name__ == "__main__":
    main()
