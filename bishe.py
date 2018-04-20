#! /usr/bin/env python
# -*- coding: utf-8 -*-
from app import app_crate
from app.main import main

from exts import db
import config

# 主程序

app = app_crate()
app.config.from_object(config)  # 导入配置文件
db.init_app(app)

if __name__ == '__main__':
    app.register_blueprint(main)
    app.run()
