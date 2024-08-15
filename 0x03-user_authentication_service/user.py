#!/usr/bin/env python3
"""
User model for a SQLAlchemy database
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

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

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new user
    new_user = User(email="user@example.com", hashed_password="hashed_pwd123")
    session.add(new_user)
    session.commit()

    # Query the user back
    user = session.query(User).filter_by(email="user@example.com").first()
    print(f"User ID: {user.id}, Email: {user.email}")
