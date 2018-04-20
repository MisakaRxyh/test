from exts import db

# 用到的主要模型

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    userID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userName = db.Column(db.String(20),nullable=False)
    userAccount = db.Column(db.String(20),nullable=False)
    userPwd = db.Column(db.String(20),nullable=False)
    Admin = db.Column(db.Integer,nullable=False)

class Statistics(db.Model):
    __tablename__ = 'statistics'
    statisticsID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    skillName = db.Column(db.String(20),nullable=False)
    positionCount = db.Column(db.Integer,nullable=False)
    firstCity = db.Column(db.String(20),nullable=False)
    secondCity = db.Column(db.String(20),nullable=False)
    thirdCity = db.Column(db.String(20),nullable=False)
    mainSalary = db.Column(db.String(20),nullable=False)
    mainEducation = db.Column(db.String(20),nullable=False)
    cityImgUrl = db.Column(db.String(100),nullable=False)
    salaryImgUrl =  db.Column(db.String(100),nullable=False)
    educationImgUrl = db.Column(db.String(100),nullable=False)
    queryDate = db.Column(db.Date,nullable=False)

class Collect(db.Model):
    __tablename__ = 'collect'
    collectID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userID = db.Column(db.Integer,db.ForeignKey('user.userID'),nullable=False)
    statisticsID = db.Column(db.Integer,db.ForeignKey('statistics.statisticsID'),nullable=False)
    collectDate = db.Column(db.Date,nullable=False)
    queryName = db.Column(db.String(20),nullable=False)

    collecter = db.relationship('User',backref= db.backref('collections'))

class Skill(db.Model):
    __tablename__ = 'skill'
    skillID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    skillName = db.Column(db.String(20),nullable=False)
    skillNum = db.Column(db.Integer,nullable=False)

class Position(db.Model):
    __tablename__ = 'position'
    positionId = db.Column(db.String(20),primary_key=True,autoincrement=True)
    positionName = db.Column(db.String(20),nullable=False)
    companyShortName = db.Column(db.String(20),nullable=False)
    city = db.Column(db.String(20),nullable=False)
    salary = db.Column(db.String(20),nullable=False)
    education = db.Column(db.String(20),nullable=False)
    workYear = db.Column(db.String(20),nullable=False)
    createTime = db.Column(db.Date,nullable=False)
    skillName = db.Column(db.String(20),nullable=False)