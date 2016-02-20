#!/usr/bin/env python

import os
import cherrypy

from .controller import Main
from .config import app_config
from .db.satool import SATool


def application(root=None, port=8070, extra={}):

    if root is None:  # serve from cwd by default
        root = os.path.abspath(os.curdir)

    config = app_config(root, extra)
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': port,
    })
    cherrypy.tree.mount(Main(), '/', config)
    cherrypy.tools.db = SATool()
    return cherrypy.tree


def start():
    application()
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    start()
