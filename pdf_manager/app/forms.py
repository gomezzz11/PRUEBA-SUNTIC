from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class UploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    file = FileField('PDF File', validators=[DataRequired()])
    approver = SelectField('Approver', validators=[DataRequired()], coerce=int)
