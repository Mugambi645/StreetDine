from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from .config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_uploads import UploadSet,configure_uploads,IMAGES
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.sessin_protection = "strong"
login_manager.login_view = "auth.login"
photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #profile blueprint
    from .profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)
    #auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
     #cart blueprint
    from .cart import cart as cart_blueprint
    app.register_blueprint(cart_blueprint)
    #cart blueprint
    from .FAQS import faqs as fag_blueprint
    app.register_blueprint(fag_blueprint)
    # configure UploadSet
    configure_uploads(app,photos)
    return app