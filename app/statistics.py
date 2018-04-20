from exts import db

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
    cityImgUrl = db.Column(db.String(20),nullable=False)
    salaryImgUrl =  db.Column(db.String(20),nullable=False)
    educationImgUrl = db.Column(db.String(20),nullable=False)
