from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class CSVForm(FlaskForm):
    # TODO validate type of file
    csv_file = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload File')

