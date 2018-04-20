#! /usr/bin/env python
# -*- coding: utf-8 -*-
#使用蓝图进行路由映射
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors,views_forms