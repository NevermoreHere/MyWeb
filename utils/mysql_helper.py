#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymysql


# 1.连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='t1', charset='utf8')