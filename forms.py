from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, InputRequired
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[InputRequired(), DataRequired()])
    password = PasswordField("Password", validators=[InputRequired(), DataRequired()])
    signup = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[InputRequired(), DataRequired()])
    password = PasswordField("Password", validators=[InputRequired(), DataRequired()])
    login = SubmitField("LET ME IN!")

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment")
    submit_comment = SubmitField("SUBMIT COMMENT")