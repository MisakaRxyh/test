from app.model import User


# 表单检验

class RegisterCheck():
    def againpwd_check(self, userpwd, againpwd):
        if userpwd == againpwd:
            return True
        else:
            return False

    def useraccount_repeat(self, useraccount):
        user = User.query.filter(User.userAccount == useraccount).first()
        if user == None:
            return True
        else:
            return False

    def is_empty(self, useraccount, username, userpwd, agaginpwd):
        if useraccount.strip() == '' or username.strip() == '' or userpwd.strip() == '' or agaginpwd.strip() == '':
            return True
        else:
            return False


class LoginCheck():
    def is_exist(self, useraccount):
        user = User.query.filter(User.userAccount == useraccount).first()
        if user == None:
            return False
        else:
            return True

    def is_vaild(self, useraccount, userpwd):
        user = User.query.filter(User.userAccount == useraccount).first()
        if user.userPwd == userpwd:
            return True
        else:
            return False

    def is_empty(self, useraccount, userpwd):
        if useraccount.strip() == '' or userpwd.strip() == '':
            return True
        else:
            return False
