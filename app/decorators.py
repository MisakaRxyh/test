from functools import wraps
from flask import session, render_template, redirect, url_for


# 登录限制的装饰器

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('userID'):
            return func
        else:
            # return redirect(url_for('login'))
            return render_template('login.html')

    return wrapper
