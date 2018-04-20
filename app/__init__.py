#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

def app_crate():
    app = Flask(__name__)
    return app