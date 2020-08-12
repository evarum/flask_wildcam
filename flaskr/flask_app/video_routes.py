from flask import (render_template)
from flaskr.flask_app.helper import get_file_meta
from flaskr.flask_app.main import app

# path for videos is specified
@app.route('/videos/<path:filename>')

# function renders template with filled in data (for videos)
def videos(filename):
    file = get_file_meta(filename)
    file['video'] = filename
    return render_template('video.html',file=file)


