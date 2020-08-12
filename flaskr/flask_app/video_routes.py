# Noah
from flask import (render_template)

from flaskr.flask_app.helper import get_file_meta
from flaskr.flask_app.main import app


@app.route('/videos/<path:filename>')
def videos(filename):
    heading = 'Filme'
    file = get_file_meta(filename)
    file['video'] = filename
    return render_template('video.html',file=file, heading=heading)


