from flask import Flask

app = Flask(__name__)
# IMPORT ABSOLUTELY NECESSARY!!!!!!!!!
from flaskr.flask_app import routes, video_routes

#def create_app(test_config=None):
    # create and configure the flask_app
    #flask_app = Flask(__name__, instance_relative_config=True)
    #flask_app.config.from_mapping(
     #   SECRET_KEY='dev',
      #  DATABASE=os.path.join(flask_app.instance_path, 'flaskr.sqlite'),
    #)

    #if test_config is None:
        # load the instance config, if it exists, when not testing
     #   flask_app.config.from_pyfile('config.py', silent=True)
    #else:
        # load the test config if passed in
     #   flask_app.config.from_mapping(test_config)

    # ensure the instance folder exists
    #try:
     #   os.makedirs(flask_app.instance_path)
    #except OSError:
     #   pass

    # a simple page that says hello


#flask_app = create_app()