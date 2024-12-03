from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class APIForm(FlaskForm):
    hour = StringField('Hour', validators=[DataRequired()])
    temperature = StringField('Temperature', validators=[DataRequired()])
    submit = SubmitField('Valider')