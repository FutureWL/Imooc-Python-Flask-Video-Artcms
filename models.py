# coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:weilai09290013@localhost:3306/artcms_pro"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

"""
用户模型
1.编号
2.账号
3.密码
4.注册时间
"""


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(20), nullable=False)  # 账号
    pwd = db.Column(db.String(100), nullable=False)  # 密码
    addtime = db.Column(db.DateTime, nullable=False)  # 注册时间

    def __repr__(self):
        return "<User %r>" % self.name


"""
文章模型
1.编号
2.标题
3.分类
4.作者
5.封面
6.内容
7.发布时间
"""


class Art(db.Model):
    __tablename__ = "art"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(100), nullable=False)  # 标题
    cate = db.Column(db.Integer, nullable=False)  # 分类
    user_id = db.Column(db.Integer, nullable=False)  # 作者
    logo = db.Column(db.Integer, nullable=False)  # 封面
    content = db.Column(db.Text, nullable=False)  # 内容
    addtime = db.Column(db.DateTime, nullable=False)  # 发布时间

    def __repr__(self):
        return "<Art %r>" % self.title


if __name__ == '__main__':
    db.create_all()
