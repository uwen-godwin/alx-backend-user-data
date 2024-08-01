#!/usr/bin/env python3
"""
Main file for reading and filtering user data.
"""

import logging
from filtered_logger import get_db, get_logger, PII_FIELDS

def main():
    """
    Main function to read and filter user data from the database.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    
    for row in cursor:
        message = "; ".join([f"{desc}={value}" for desc, value in zip(cursor.column_names, row)])
        logger.info(message)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
