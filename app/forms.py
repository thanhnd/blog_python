from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length

class LoginForm(Form):
    email = StringField('email',
        validators = [DataRequired('Please enter your email'),
            Email('Invalid Email')])
    password = PasswordField('password',
        validators = [DataRequired('Please enter your password')])
    remember_me = BooleanField('remember_me', default = False)

class RegisterForm(Form):
    email = StringField('email',
        validators = [DataRequired('Please enter your email'),
            Email('Invalid Email')])
    password = PasswordField('password',
        validators = [DataRequired('Please enter your password')])
    confirm_password = PasswordField('confirm_password',
        validators = [DataRequired('Please enter your confirm password'),
            EqualTo('password', 'Passwords must match')])

class ChangePasswordForm(Form):
    password = PasswordField('New Password', [InputRequired(),
        EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')

class CreatePostForm(Form):
    title = StringField('title', validators = [DataRequired()])
    content = TextAreaField('content', validators = [DataRequired()])
