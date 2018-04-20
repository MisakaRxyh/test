#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

# 配置文件

DEBUG = True


# sqlalchemy连接数据库
# 固定格式:
# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhaopin_info'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME
                                                                       , PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)
SESSION_COOKIE_AGE = 60 * 30
SESSION_EXPIRE_AT_BROWSER_CLOSE = False


class DBConfig:
    DB_HOST = '127.0.0.1'
    DB_NAME = 'zhaopin_info'
    DB_USER = 'root'
    DB_PASSWD = '123456'
    DB_PORT = 3306
    DB_CHARSET = 'utf8'
