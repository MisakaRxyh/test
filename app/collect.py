from exts import db

class Collect(db.Model):
    __tablename__ = 'collect'
    collectID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userID = db.Column(db.Integer,db.ForeignKey('user.userID'),nullable=False)
    statisticsID = db.Column(db.Integer,db.ForeignKey('statistics.statisticsID'),nullable=False)
    collectDate = db.Column(db.String(20),nullable=False)
    queryName = db.Column(db.String(20),nullable=False)

    collecter = db.relationship('User',backref= db.backref('collections'))
    #collectinfo = db.relationship('Statistics',backref= db.backref('collections'))
    #collect = Collect(...)
    #collect.collecter = User.query.filter(User.userID == 1).first()
    #collecter.collections

    #collect = Collect.query.filter(Collect.collectID == 1).first()
    #print collect.collecter.userName
    #print collect.collectinfo.statisticsID

    #user = User.query.filter(User.UserID == 1).first()
    #result =user.collections

    #stat = Statistics.query.filter(Statistics.StatisticsID == 1).first()
    #
