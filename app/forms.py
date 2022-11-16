from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class ManagerTeamForm(FlaskForm):
    manager_name = StringField('Manager Name', validators=[DataRequired()])
    team = StringField('Team Name', validators=[DataRequired()])
    start_date = DateField('Start Date')
    end_date = DateField('End Date')

    submit = SubmitField('Submit')