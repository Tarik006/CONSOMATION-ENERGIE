from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange


class APIForm(FlaskForm):
    humidity = IntegerField('humidity', validators=[DataRequired(), NumberRange(min=0, max=100)])
    temperature = IntegerField('Temperature', validators=[DataRequired(), NumberRange(min=0, max=45)])
    zone = SelectField('Choisissez une zone', choices=[('PowerConsumption_Zone1', 'Zone 1'), ('PowerConsumption_Zone2', 'Zone 2'), ('PowerConsumption_Zone3', 'Zone 3')],validators=[DataRequired()] )

    submit = SubmitField('Valider')