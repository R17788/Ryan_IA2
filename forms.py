from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class LoginInformation(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


class DJSearch(FlaskForm):
    search = StringField('Search for DJ:')
    category = SelectField('category',
                           choices=[("first_name", "First Name"), ("last_name", "Last Name"), ("email", "Email")])


class ArtistSearch(FlaskForm):
    search = StringField('search')
    category = SelectField('category',
                           choices=[("details", "All Details"), ("albums", "Albums")])


class DjEventSearch(FlaskForm):
    search = StringField('search')
    category = SelectField('category',
                           choices=[("ID", "Event ID"), ("name", "Event Name"), ("venue", "Event Location")])
