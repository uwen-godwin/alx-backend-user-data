#!/usr/bin/env python3
""" Blueprint for API views
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import the views to register routes
from api.v1.views.index import *
from api.v1.views.users import *
