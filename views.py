# coding:utf8
import datetime
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, flash
from forms import LoginForm, RegisterForm, ArtForm
from models import User, db
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

# 登录
@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title=u"登录", form=form)  # 渲染模版


# 注册
@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        # 保存数据
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db.session.add(user)
        db.session.commit()
        # 定义一个会话闪现
        flash(u"注册成功，请登录!", "ok")
        return redirect("/login/")
    else:
        flash(u"注册失败，请重新登录!", "err")
        return redirect("/register/")
    return render_template("register.html", title=u"注册", form=form)  # 渲染模版


# 退出(302跳转到登录页面)
@app.route("/logout/", methods=["GET"])
def logout():
    return redirect("/login")


# 发布文章
@app.route("/art/add/", methods=["GET", "POST"])
def art_add():
    form = ArtForm()
    return render_template("art_add.html", title=u"发布文章", form=form)


# 编辑文章
@app.route("/art/edit/<int:id>/", methods=["GET", "POST"])
def art_edit(id):
    return render_template("art_edit.html")


# 删除文章
@app.route("/art/del/<int:id>/", methods=["GET"])
def art_del(id):
    return redirect("/art/list/")


# 文章列表
@app.route("/art/list/", methods=["GET"])
def art_list():
    return render_template("art_list.html", title=u"文章列表")


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8888)
