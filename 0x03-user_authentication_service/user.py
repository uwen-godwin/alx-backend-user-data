#!/usr/bin/env python3
"""
User model for a SQLAlchemy database
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base  # Corrected import for declarative_base

Base = declarative_base()

class User(Base):
    """ User class definition """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

if __name__ == "__main__":
    # Create an SQLite database and the User table
    engine = create_engine('sqlite:///a.db')
    Base.metadata.create_all(engine)
