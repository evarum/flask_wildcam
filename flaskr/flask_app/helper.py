import os

from flaskr.flask_app.config import PATH, ENDUNG


def get_file_meta(filename):
    meta = {}
    meta['filename'] = filename
    meta['date'] = 'u'
    meta['time'] = 't'

    return meta


def data_to_html_file():
    direc = PATH
    ext = ENDUNG
    files = []
    for i in os.listdir(direc):
        if os.path.splitext(i)[1] == ext:
            meta = get_file_meta(i)
            files.append(meta)

    #file_loader = FileSystemLoader('templates')
    #env = Environment(loader=file_loader)
    #template = env.get_template('showimage.jinja')

    return files