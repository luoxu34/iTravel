# -*- coding: utf-8 -*-

from sanic import Blueprint
from .hello import hello_bp


api = Blueprint.group(hello_bp, url_prefix="/api")

