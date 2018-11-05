from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('请问你的名字是?', validators=[DataRequired()])
    # email = StringField('请输入你的邮箱', validators=[Email('请填写正确的电子邮箱地址')])
    submit = SubmitField('Submit')
