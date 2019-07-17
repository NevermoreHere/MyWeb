#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tornado.web
import logging
from datetime import datetime



class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("visit basehandler {}".format(datetime.now()))
        self.write("base_index")

    def post(self, *args, **kwargs):
        pass

