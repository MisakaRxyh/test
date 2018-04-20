#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, session, g, request
from app.model import User, Statistics, Collect, Skill
from exts import db
from . import main
from app.decorators import login_required
import datetime

import spider

# 主要路由映射

# 所谓路由映射 就是flask框架提供的url路由—>视图函数的映射
# route('/xxx')里的xxx就是在浏览器中输入的url
# 下方定义的 def函数 就是对应的视图函数
# 当在浏览器中输入url地址时 会调用视图函数

@main.route('/')  # 默认地址 127.0.0.1/
@main.route('/index')  # 主页地址 127.0.0.0/index 当在浏览器中输入这两个地址时会执行index()函数
def index():
    user = g.user  # g是flask中自带的全局变量 全局变量在任何视图函数中都可以使用 可以存放对象 保存用户
    return render_template('index.html', user=user,
                           skill=g.skill)  # render_template()的作用是跳转到templates文件夹下的html页面中 后面的参数是传递到页面中


@main.route('/simple')  # 简单查询
def simple():
    user = g.user
    return render_template('simple.html', user=user)  # 比如在simple.html页面中 就可以使用 {{user}}的方式来读取user的值


@main.route('/count')  # 统计查询
def count():
    user = g.user
    return render_template('count.html', user=user)


@main.route('/logout')  # 用户登出
def logout():
    # session['userID'] = None  # session是服务器缓存 用来保存用户id 实现保存登录信息的功能
    session.pop('userID', None)  # 将userID从session中删除 实现用户登出的功能
    return render_template('index.html', skill=g.skill)


@main.route('/home')  # 个人主页
def user_home():
    user = g.user
    collections = user.collections  # 获取当前用户的收藏信息 collections是一个列表
    for collection in collections:
        print(collection.collectDate)
    return render_template('home.html', user=user, collections=collections)


@main.route('/admin')  # 后台管理
def admin():
    user = g.user
    return render_template('admin.html', user=user)

@main.route('/userlist')
def userlist():
    user = g.user
    user_list = User.query.all()
    return render_template('userlist.html',user = user,user_list = user_list)


@main.route('/spider', methods = ['GET','POST'])
def spider():
    if request.method == 'GET':
        user = g.user
        return render_template('spider.html',user = user)
    else:
        return



@main.route('/collect')  # 收藏功能
def collect():
    statisticsID = request.args.get('statisticsID')  # 获取url中的参数 statisticsID 统计信息表中的ID
    # 一般浏览器与服务器传输数据有两种方式 GET和 POST
    # GET方法一般从服务器获取数据不对服务器造成影响 通过url传参数 比如百度python会看到浏览器上的搜索栏内容如下
    # https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=9&tn=98012088_6_dg&wd=python&oq=pycharm%25E5%25AF%25BC%25E5%2587%25BArequirement%25E6%2596%2587%25E4%25BB%25B6&rsv_pq=87ee94770000a13e&rsv_t=827bWDC3Mjm7oY3z67M%2F%2F9thxK1vGCXjMALR56I%2BTho%2B0rqP84oh2BTH79qK0jBiEj8v1g&rqlang=cn&rsv_enter=1&rsv_sug3=1&rsv_sug2=0&inputT=1565&rsv_sug4=1565
    # 其中/s 是路径 就比如我这里的/collect
    # 后面的？及其后面的内容不参与url路由映射
    # ？后面的 ie=utf-8&中 ie是参数名，utf-8是参数值 &符号是连接符，连接后面的参数
    # 如果我想获取 参数ie 的值 那么就可以用 a = request.args.get('ie')
    # 变量a 的结果就是utf-8
    # POST方法一般用于上传数据给服务器 通过表单获取参数 在views_forms.py文件中详细解释
    print(statisticsID)
    user = g.user
    stat = Statistics.query.filter(Statistics.statisticsID == statisticsID).first()
    # 这是sqlalchemy模块中的语句 用来进行数据库查询的 结果就是在数据库的statistics表中找到ID为从url中获取的statisticsID的那条记录并保存为对象
    collectdate = datetime.date.today()
    collection = Collect(
            userID=user.userID,
            statisticsID=statisticsID,
            collectDate=collectdate,
            queryName=stat.skillName,
    )  # 创建一个收藏对象 也就是一个收藏记录 如果表中没有这个记录就保存到数据库中
    statids = []
    for collections in user.collections:
        statids.append(str(collections.statisticsID))
    print(statids)
    print(collection.statisticsID)
    if str(collection.statisticsID) not in statids:
        db.session.add(collection)  # 保存到数据库中
        db.session.commit()  # 提交这次保存操作
        return "收藏成功"
    else:
        return "已经收藏过了"


@main.route('/detail')  # 收藏详情
def detail():
    statisticsID = request.args.get('statisticsID')
    print(statisticsID)
    user = g.user
    stat = Statistics.query.filter(Statistics.statisticsID == statisticsID).first()  # 从数据库中找到对应的statisticsID记录
    return render_template('detail.html', stat=stat, user=user)


@main.route('/delete')  # 删除收藏
def delete():
    statisticsID = request.args.get('statisticsID')
    user = g.user
    collection = Collect.query.filter(Collect.statisticsID == statisticsID).first()
    db.session.delete(collection)  # 删除
    db.session.commit()
    collections = user.collections
    return render_template('home.html', user=user, collections=collections)


@main.before_request  # 钩子函数 在路由函数之前执行
def get_session_user():
    userid = session.get('userID')  # 在session中获取用户id 实现用户登录缓存的功能
    user = User.query.filter(User.userID == userid).first()
    g.user = user  # 将session中获取到的id对应的用户保存到全局变量g中
    skill = Skill.query.all()  # 将数据库skill表中所有信息提取出来 以便主页展示
    g.skill = skill
