#!/usr/bin/python
# -*- coding: UTF-8 -*-

from utils.config import USER_TYPE


class user_model:
    def __init__(self, user_name, user_password):
        self.type = USER_TYPE
        self.user_name = user_name
        self.user_password = user_password

    def get_info(self):
        print self.type, self.user_name, self.user_password

    def get_favorite(self):
        print "favorite list:"
