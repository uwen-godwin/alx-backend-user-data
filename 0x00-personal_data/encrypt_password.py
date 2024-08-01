#!/usr/bin/env python3
"""
Module for handling password encryption.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password with a salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to check.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
