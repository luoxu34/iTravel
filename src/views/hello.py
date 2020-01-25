# -*- coding: utf-8 -*-

from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import text


class Hello(HTTPMethodView):
    
    HELLO = "Hello World!"
    
    async def get(self, request):
        return text(Hello.HELLO)
    
    async def post(self, request):
        return text(Hello.HELLO)


hello_bp = Blueprint("hello", url_prefix="/")
hello_bp.add_route(Hello.as_view(), "hello")

