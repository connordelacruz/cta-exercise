import csv
from flask import render_template
from cta import app
from cta.forms import CSVForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CSVForm()
    # If POST data is received and validated, parse CSV and render results
    if form.validate_on_submit():
        file_string = form.csv_file.data.read().decode('utf-8')
        reader = csv.DictReader(file_string.splitlines())
        fields = reader.fieldnames
        # TODO remove duplicates, sort by RUN_NUMBER
        data = [row for row in reader]
        return render_template(
            'index.html', title='Upload File',
            form=form, results=True, data=data,
            fields=fields
        )
    # Render index.html on GET request
    return render_template('index.html', title='Upload File', form=form, results=False)

