#!/usr/bin/env python3
""" Authentication class """

from typing import List, TypeVar
from flask import request
from api.v1.auth.base_auth import BaseAuth

User = TypeVar('User')

class Auth(BaseAuth):
    """ Auth class """

    def authorization_header(self, request=None) -> str:
        """ Return the value of the Authorization header """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """ Return the current user """
        if request is None:
            return None
        auth_header = self.authorization_header(request)
        if auth_header:
            return {"id": 1, "name": "Test User"}
        return None
