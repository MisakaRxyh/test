from exts import db

class User(db.Model):
    __tablename__ = 'user'
    userID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userName = db.Column(db.String(20),nullable=False)
    userAccount = db.Column(db.String(20),nullable=False)
    userPwd = db.Column(db.String(20),nullable=False)
