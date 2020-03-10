from flask import render_template
from cta import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # TODO render_template() on GET, parse data on POST
    return render_template('index.html', title='Upload File')

