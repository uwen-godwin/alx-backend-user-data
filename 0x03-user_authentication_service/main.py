#!/usr/bin/env python3
"""
Main file to test the functionality of the user authentication service
"""

from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("Successfully created a new user!")
except ValueError as err:
    print(f"Could not create a new user: {err}")

try:
    user = auth.register_user(email, password)
    print("Successfully created a new user!")
except ValueError as err:
    print(f"Could not create a new user: {err}")
