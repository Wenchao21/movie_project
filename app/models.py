from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
import pymysql

# 这个app,仅仅为链接数据库使用的,不是app里面那个app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password110@127.0.0.1/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)
    phone = db.Column(db.String(100), unique = True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique = True)
    addtime = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    uuid = db.Column(db.String(255), unique = True)
    userlogs = db.relationship('Userlog', backref = 'user')

    def __repr__(self):
        return "<User %r>"% self.name

class UserLog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index = True, default = datetime.utcnow)

    def __repr__(self):
        return "<Userlog %r>"% self.id


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    addtime = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    movies = db.relationship("Movie", backref = 'tag')

    def __repr__(self):
        return "<Tag %r>"% self.name

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), unique = True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))

    def __repr__(self):
        return "<Movie %r>"% self.title

class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), unique = True)
    logo = db.Column(db.String(255), unique = True)
    addtime = db.Column(db.DateTime, index = True, default = datetime.utcnow())

    def __repr__(self):
        return "<preview %r>"% self.title



if __name__ == "__main__":
    db.create_all()
    print("create all!!!")
    print("ccccccccc")
