#!/usr/bin/env python3
"""
Module for logging related functions and classes.
"""

import logging
import os
import mysql.connector
from typing import List, Tuple

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates the fields in the log message.
    
    Args:
        fields: List of fields to obfuscate.
        redaction: The string to replace the field values with.
        message: The log message to be obfuscated.
        separator: The character that separates the fields in the message.
    
    Returns:
        The obfuscated log message.
    """
    import re
    regex = '|'.join([f'{field}=[^;]*' for field in fields])
    return re.sub(regex, lambda x: f"{x.group().split('=')[0]}={redaction}", message)

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str]):
        """
        Initialize the formatter with fields to obfuscate.
        
        Args:
            fields: The fields to obfuscate in log messages.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, obfuscating specified fields.
        
        Args:
            record: The log record to be formatted.
        
        Returns:
            The formatted log record as a string.
        """
        return filter_datum(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)

def get_logger() -> logging.Logger:
    """
    Create and configure a logger instance.
    
    Returns:
        The configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)
    return logger

PII_FIELDS: Tuple[str] = ("email", "phone", "ssn", "password", "user_agent")

def get_db():
    """
    Create and configure a MySQL database connection.
    
    Returns:
        The database connection object.
    """
    import os
    import mysql.connector
    return mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
