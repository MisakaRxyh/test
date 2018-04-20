#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
from config import DBConfig


# 数据库操作

class MySQL_DB():
    def __init__(self,
                 host=DBConfig.DB_HOST,
                 name=DBConfig.DB_NAME,
                 user=DBConfig.DB_USER,
                 passwd=DBConfig.DB_PASSWD,
                 port=DBConfig.DB_PORT,
                 charset=DBConfig.DB_CHARSET
                 ):
        self.host = host
        self.name = name
        self.user = user
        self.passwd = passwd
        self.port = port
        self.charset = charset

        self.conn = None
        self.cursor = None

    def dbconn(self):
        try:
            conn = pymysql.connect(
                    host=self.host, user=self.user, passwd=self.passwd, db=self.name, charset=self.charset,
                    port=self.port
            )
            self.conn = conn
            self.cursor = conn.cursor()
            print("connect success")
        except pymysql.Error as e:
            print("connect error :", e)

    def insert(self, info):
        insertsql = "insert into position values(%(positionId)s,%(positionName)s,%(companyShortName)s,%(city)s,%(salary)s,%(education)s,%(workYear)s,%(createTime)s,%(skillName)s)"
        if self.conn:
            try:
                self.cursor.execute(insertsql, info)
                print("insert success")
                print(info['skillName'])
                updatesql = "update skill set skillNum = skillNum +1 where skillName = '" + info['skillName'] + "'"
                self.update(updatesql)
            except pymysql.Error as e:
                print("insert error :", e)
                self.conn.rollback()
            else:
                self.conn.commit()

    def update(self, sql):
        if self.conn:
            try:
                self.cursor.execute(sql)
                print("update success")
            except pymysql.Error as e:
                print("update error :", e)
                self.conn.rollback()
            else:
                self.conn.commit()

    def delete(self, sql):
        if self.conn:
            try:
                self.cursor.execute(sql)
                print("delete success")
            except pymysql.Error as e:
                print("delete error :", e)
                self.conn.rollback()
            else:
                self.conn.commit()

    def select(self, sql):
        if self.conn:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        return results

    def close(self):
        if self.conn:
            self.conn.close()
            print("datebase close")
