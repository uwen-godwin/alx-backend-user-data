#!/usr/bin/env python3
"""
Module to handle logging and database operations with sensitive data filtering.
"""

import logging
import mysql.connector
import os
import re
from typing import List, Any
import bcrypt

PII_FIELDS = ("email", "phone", "ssn", "password", "name")

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates the specified fields in the log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): Redaction string.
        message (str): Log message.
        separator (str): Separator character used in the log message.

    Returns:
        str: Obfuscated log message.
    """
    pattern = '|'.join([f'{field}=[^;]*' for field in fields])
    return re.sub(pattern, lambda match: f'{match.group().split("=")[0]}={redaction}', message)

class RedactingFormatter(logging.Formatter):
    """
    Custom logging formatter to redact sensitive information.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes RedactingFormatter with fields to redact.

        Args:
            fields (List[str]): List of fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record.

        Args:
            record (logging.LogRecord): Log record to format.

        Returns:
            str: Formatted log record.
        """
        return filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)

def get_logger() -> logging.Logger:
    """
    Creates and configures a logger.

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

def get_db() -> Any:
    """
    Creates a database connection using credentials from environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection.
    """
    return mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )

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

def main() -> None:
    """
    Main function to read and filter data from the database.
    """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        logger.info("name=%s; email=%s; phone=%s; ssn=%s; password=%s; ip=%s; last_login=%s; user_agent=%s;",
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
