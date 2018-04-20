#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from flask import session
from flask import g
from . import main
from app.mysqldb import MySQL_DB
from app.parse import Parse
from app.drawimg import Drawimg
from app.model import User, Statistics, Position
from exts import db
from app.formcheck import LoginCheck, RegisterCheck
import datetime

# test 导包
import json

# 表单中的路由映射
#

@main.route('/simple_query') # 简单查询 将数据库中的爬取的职位信息全部展示出来
def simple_query():
    user = g.user
    page = request.args.get('page', 1, type=int) #分页
    search = request.args.get('search') #获取查询内容
    pagination = Position.query.filter(Position.skillName == search).order_by(Position.createTime.desc()).paginate(page,
                                                                                                                   per_page=20,
                                                                                                                   error_out=False)
    result = pagination.items #分页功能
    return render_template('simple.html', search=search, result=result, user=user, pagination=pagination)

#测试
@main.route('/test')
def test():
    return render_template('test.html')


@main.route('/count_query') #
def count_query():
    dd = MySQL_DB()
    dd.__init__()
    dd.dbconn()
    sql = "select * from position where skillName like '%" + request.args.get('search') + "%'"
    if request.args.get('search') == '':
        context = {
            'result': None,
            'name': '',
            'user': g.user,
            'statisticsID': None,
        }
        return render_template('count.html', **context)
    else:
        result = dd.select(sql)
        name = request.args.get('search')
        pc = Parse.PositionCount(result)
        cp = Parse.CityParse(result)
        sp = Parse.SalaryParse(result)
        ep = Parse.EducationParse(result)

        cpath = Drawimg.draw(cp, name, 'city')
        spath = Drawimg.draw(sp, name, 'salary')
        epath = Drawimg.draw(ep, name, 'education')

        path = {
            'cpath': Parse.pathParse(cpath),
            'spath': Parse.pathParse(spath),
            'epath': Parse.pathParse(epath),
        }
        result = Position.query.filter(Position.skillName)
        result = Parse.resultParse(name, pc, cp, sp, ep)
        result['path'] = path
        if g.user == None:
            context = {
                'result': result,
                'name': name,
                'user': g.user,
                'statisticsID': -1,
            }
            return render_template('count.html', **context)
        else:
            stat = Statistics(
                    skillName=result['skillName'],
                    positionCount=result['positionCount'],
                    firstCity=result['mainCity']['firstCity'],
                    secondCity=result['mainCity']['secondCity'],
                    thirdCity=result['mainCity']['thirdCity'],
                    mainSalary=result['mainSalary'],
                    mainEducation=result['mainEducation'],
                    cityImgUrl=result['path']['cpath'],
                    salaryImgUrl=result['path']['spath'],
                    educationImgUrl=result['path']['epath'],
                    queryDate=datetime.date.today()
            )
            print(stat)
            querydates = []
            for stats in Statistics.query.filter(Statistics.skillName == stat.skillName):
                querydates.append(stats.queryDate)
            print(querydates)
            print(stat.queryDate)
            if stat.queryDate not in querydates:
                db.session.add(stat)
                db.session.commit()

            else:
                stat = Statistics.query.filter(Statistics.skillName == stat.skillName,
                                               Statistics.queryDate == stat.queryDate).first()
            print(stat.statisticsID)
            dd.close()

            context = {
                'result': result,
                'name': name,
                'user': g.user,
                'statisticsID': stat.statisticsID
            }
            return render_template('count.html', **context)


# 下面的登录与注册就用到了POST方法
# route函数默认是使用GET方法 所以要写明方法是用GET还是POST
# 简单来说 通过url跳转就是GET方法 通过表单提交就是POST方法
# 这里登录和注册都用到了GET和POST方法
# 因为转到登录注册页面是GET方法
# 通过表单提交是POST方法
# 可以去看一下templates文件夹下的login.html里的
#     <div class="form-group">
#         <h1>登录</h1>
#         <form method="post" action="/login" onsubmit="return validate_form(this)">
#             <label>账号</label><input class="form-control" type="text" id="txt_username" name="useraccount"><br>
#             <label>密码</label><input class="form-control" type="password" id="txt_userpwd" name="userpwd"><br>
#
#             <input type="checkbox" id="ck_rmbUser" name="isRmbUser">一个月内自动登录
#             <input class="btn btn-default" type="submit" id="sub" value="登录">
#         </form>
#     </div>
# 这段代码 form标签里的method是post action是/login  也就是说 当点击登录按钮提交表单中的登录信息时
# 会通过action 映射到下面登录的/login路由上 执行user_login()函数

@main.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET': # 获取访问方式 如果是GET 就转到登录页面
        return render_template('login.html')
    else:                       # 如果是POST 就进行登录验证
        useraccount = request.form.get('useraccount')
        userpwd = request.form.get('userpwd')
        isRmbUser = request.form.get('isRmbUser')
        lc = LoginCheck()
        if lc.is_empty(useraccount=useraccount, userpwd=userpwd):
            error = '请确认用户名或密码填写完整'
            return render_template("error.html", error=error)
        elif not lc.is_exist(useraccount):
            error = '用户名不存在，请检查'
            return render_template("error.html", error=error)
        elif not lc.is_vaild(useraccount, userpwd):
            error = '密码错误，请重新输入'
            return render_template('error.html', error=error)
        else:
            print('success')
            user = User.query.filter(User.userAccount == useraccount).first()
            print(user)
            print(user.userID)
            session['userID'] = user.userID
            if isRmbUser == 'on':
                session.permanent = True
            return render_template('index.html', user=user, skill=g.skill)


@main.route('/register', methods=['GET', 'POST']) # 注册功能
def user_register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        useraccount = request.form.get('useraccount')
        username = request.form.get('username')
        userpwd = request.form.get('userpwd')
        againpwd = request.form.get('againpwd')

        rc = RegisterCheck()
        if rc.is_empty(useraccount, username, userpwd, againpwd):
            error = '请确认注册信息填写完整'
            return render_template('error.html', error=error)
        elif not rc.againpwd_check(userpwd, againpwd):
            error = '密码重复错误，请重新输入'
            return render_template('error.html', error=error)
        elif not rc.useraccount_repeat(useraccount):
            error = '此账号已经被注册'
            return render_template('error.html', error=error)
        else:
            user = User(
                    userName=username,
                    userAccount=useraccount,
                    userPwd=userpwd,
                    Admin=0,  # 注册用户默认没有管理员权限
            )
            db.session.add(user)
            db.session.commit()
            userid = User.query.filter(User.userAccount == useraccount).first().userID
            session['userID'] = userid
            return render_template('success.html', user=user)

