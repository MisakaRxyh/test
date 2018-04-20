from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from bishe import app
from exts import db
from app.model import User, Statistics, Collect, Skill, Position

# ORM 实体关系模型
# 利用flask_script flask_migrate 模块完成数据库的创建 更新 和迁移

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

    # python manage.py db init
    # python manage.py db migrate
    # python manage.py db upgrade
    # 模型 -> 迁移文件 -> 表
