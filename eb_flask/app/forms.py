from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class SignUpForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email(message="Not a valid Email")])
    mobile = IntegerField()
    country = StringField(validators=[DataRequired()])
    newsletter = BooleanField('Weekly Digest')
    submit = SubmitField()
