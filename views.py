# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-01-18
# Author: juzi
# E-mail: jentlewoo@gmail.com


import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", title="登录")

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html", title="Tornado Application")

class InfoHandler(BaseHandler):
    def post(self):
        user = self.get_argument("arg1")
        password = self.get_argument("arg2")
        self.db.execute("insert into user(username,password) values(%s,%s)", user, password)
        self.render("info.html", arg1=user, arg2=password, title="info - mysql")

class ListHandler(BaseHandler):
    def get(self):
        ret = self.db.query("select * from user")
        self.render("list.html",arg = ret, title="all user")
    """
for article in db.query("SELECT * FROM articles"):
        print article.title
    """