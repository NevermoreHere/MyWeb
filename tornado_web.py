#!/usr/bin/python
# -*- coding: UTF-8 -*-


import tornado.ioloop
import tornado.web
import os
import logging

from controller.BaseHandler import BaseHandler

logging.basicConfig(level=logging.DEBUG)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", BaseHandler),
                    ]
        setting = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **setting)


def main():
    Application().listen(8888, xheaders=True)
    logging.info("=== tornado server start ===")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
