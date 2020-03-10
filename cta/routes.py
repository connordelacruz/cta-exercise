from flask import render_template
from cta import app
from cta.forms import CSVForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CSVForm()
    # If POST data is received and validated, parse CSV and render results
    if form.validate_on_submit():
        # TODO
        return 'Nice!'
    # Render index.html on GET request
    return render_template('index.html', title='Upload File', form=form)

