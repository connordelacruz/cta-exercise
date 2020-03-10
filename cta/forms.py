from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class CSVForm(FlaskForm):
    csv_file = FileField(validators=[
        FileRequired(),
        FileAllowed(['csv'], 'Please upload a valid CSV file')
    ])
    submit = SubmitField('Upload File')

