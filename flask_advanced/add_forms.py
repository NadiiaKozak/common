import uuid

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField, TextAreaField, BooleanField, FloatField, validators
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):

    id = str(uuid.uuid4())
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = IntegerField('price', [validators.NumberRange(min=0), validators.DataRequired()])
    image = FileField(validators=[DataRequired()])
    submit = SubmitField()


class SupermarketForm(FlaskForm):
    id = str(uuid.uuid4())
    name = StringField('name', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField(validators=[DataRequired()])
    submit = SubmitField()
