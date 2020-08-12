from flaskr.flask_app.config import PATH
from flaskr.flask_app.main import app
from flask import (render_template, send_from_directory)
from flaskr.flask_app.helper import data_to_html_file

@app.route('/')
@app.route('/index')
def index( *args):
    heading = 'Filme'
    files = data_to_html_file()
    # render template with filled in data
    return render_template('test_wc.html',files=files, heading=heading)

# path for pictures is specified
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(PATH, filename)