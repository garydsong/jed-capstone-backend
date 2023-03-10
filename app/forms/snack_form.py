from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError

from app.models import Snack
# this is the classes on all the snack objects i am making


class SnackForm(FlaskForm):
    name = StringField('Snack Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    img = StringField('Snack Image', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
