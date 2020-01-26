#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import uvloop
from sanic import Sanic
from views import api
from settings import Config


def create_app() -> Sanic:
    app = Sanic(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app: Sanic):
    pass


def register_blueprints(app: Sanic):
    app.blueprint(api)


if __name__ == "__main__":
    app = create_app()
    asyncio.set_event_loop(uvloop.new_event_loop())
    server = app.create_server(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG, return_asyncio_server=True)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(server)
    try:
        loop.run_forever()
    except:
        loop.stop()

