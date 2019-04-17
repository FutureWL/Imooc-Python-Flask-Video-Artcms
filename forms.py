# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import User

""""
登录表单：
1.账号
2.密码
3.登录按钮
"""


class LoginForm(FlaskForm):
    name = StringField(
        label=u"账号",
        validators=[],
        description=u"账号",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入账号!"
        }
    )

    pwd = PasswordField(
        label=u"密码",
        validators=[],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码!"
        }
    )

    submit = SubmitField(
        u"登录",
        render_kw={
            "class": "btn btn-primary"
        }
    )


""""
注册表单：
1.账号
2.密码
3.确认密码
4.验证码
3.注册按钮
"""


class RegisterForm(FlaskForm):
    name = StringField(
        label=u"账号",
        validators=[
            DataRequired(u"账号不能为空!")
        ],
        description=u"账号",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入账号!"
        }
    )

    pwd = PasswordField(
        label=u"密码",
        validators=[
            DataRequired(u"密码不能为空!")
        ],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码!"
        }
    )

    repwd = PasswordField(
        label=u"确认密码",
        validators=[
            DataRequired(u"确认密码不能为空!"),
            EqualTo('pwd', message=u"两次输入密码不一致！")
        ],
        description=u"确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入确认密码!"
        }
    )

    code = StringField(
        label=u"验证码",
        validators=[
            DataRequired(u"验证码不能为空!")
        ],
        description=u"验证码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入验证码!"
        }
    )

    submit = SubmitField(
        u"注册",
        render_kw={
            "class": "btn btn-success"
        }
    )

    # 自定义字段验证规则：validate_字段名
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user > 0:
            raise ValidationError(u"账号已存在，不能重复注册！")


""""
发布文章表单：
1.标题
2.分类
3.封面
4.内容
3.发布文章按钮
"""


class ArtForm(FlaskForm):
    title = StringField(
        label=u"标题",
        description=u"标题",
        validators=[],
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入标题!"
        }
    )
    cate = SelectField(
        label=u"分类",
        description=u"分类",
        validators=[],
        choices=[(1, u"科技"), (2, u"搞笑"), (3, u"军事")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    logo = FileField(
        label=u"封面",
        description=u"封面",
        validators=[],
        render_kw={
            "class": "form-control-file"
        }
    )
    content = TextAreaField(
        label=u"内容",
        description=u"内容",
        validators=[],
        render_kw={
            "style": "height:300px;",
            "id": "content"
        }
    )
    submit = SubmitField(
        u"发布文章",
        render_kw={
            "class": "btn btn-primary"
        }
    )
