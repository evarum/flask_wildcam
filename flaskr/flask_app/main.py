from flask import Flask

app = Flask(__name__)
# IMPORT ABSOLUTELY NECESSARY!!!!!!!!!
from flaskr.flask_app import routes, video_routes
