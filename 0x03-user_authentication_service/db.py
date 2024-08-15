#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError, NoResultFound

from user import Base, User
from typing import Dict


class DB:
    """DB class for interacting with the database."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Creates a new user and adds them to the database.
        
        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.
        
        Returns:
            User: The newly created User object.
        """
        session = self._session
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs: Dict) -> User:
        """Find a user by arbitrary keyword arguments.
        
        Args:
            **kwargs (Dict): Arbitrary keyword arguments to search for.
        
        Returns:
            User: The user object that matches the given criteria.
        
        Raises:
            NoResultFound: If no user was found with the provided criteria.
            InvalidRequestError: If the provided criteria is invalid.
        """
        session = self._session
        try:
            user = session.query(User).filter_by(**kwargs).one()
        except (InvalidRequestError, NoResultFound) as e:
            raise e

        return user
