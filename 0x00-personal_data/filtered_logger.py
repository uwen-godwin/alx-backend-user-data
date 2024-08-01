#!/usr/bin/env python3
"""
Module for connecting to the database.
"""

import os
import mysql.connector
from mysql.connector import connection

def get_db() -> connection.MySQLConnection:
    """
    Connects to the MySQL database using environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection.
    """
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "my_db")

    return mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
