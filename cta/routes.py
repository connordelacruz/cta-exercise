from flask import render_template
from cta import app
from cta.forms import CSVForm
from cta.utils import parse_csv

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CSVForm()
    # If POST data is received and validated, parse CSV and render results
    if form.validate_on_submit():
        file_string = form.csv_file.data.read().decode('utf-8')
        fields, data = parse_csv(file_string)
        return render_template(
            'index.html', title='Upload File',
            form=form, results=True, data=data,
            fields=fields
        )
    # Render index.html on GET request
    return render_template('index.html', title='Upload File', form=form, results=False)

