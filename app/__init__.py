import boto3
import os

from .admin.views import CompanyView, JobView, StatisticsView, StreamView, UserView
from flask import Flask, g, request
from flask_admin import Admin
from flask_admin.base import MenuLink
from flask_assets import Environment
from flask_babelex import Babel, Domain
from flask_bcrypt import Bcrypt
from flask_cdn import CDN
from flask_login import LoginManager
from flask_qrcode import QRcode
from flask_sslify import SSLify
from pymongo import MongoClient


# Storage init
def get_db():
    with app.app_context():
        if not hasattr(g, 'db'):
            client = MongoClient(host=os.environ.get('MONGODB_URI'))
            g.db = client.get_default_database()
        return g.db


# App init
app = Flask(__name__, template_folder='templates')
app.debug = bool(os.environ.get('DEBUG', False))
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'my_debug_key')
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('FLASK_PASSWORD_SALT', 'my_debug_salt')
app.config['TOKEN_EXPIRATION'] = int(os.environ.get('TOKEN_EXPIRATION', 7200))
app.config['PASSWORD_TOKEN_EXPIRATION'] = int(os.environ.get('PASSWORD_TOKEN_EXPIRATION', 600)) #needs to be shorter for security reasons
app.config['CDN_DOMAIN'] = os.environ.get('CLOUDFRONT_DOMAIN')
app.config['CDN_DEBUG'] = app.debug
app.config['CDN_HTTPS'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['BABEL_DEFAULT_LOCALE'] = 'fr'
app.jinja_env.add_extension('jinja2_time.TimeExtension')

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Bcrypt
bcrypt = Bcrypt()
bcrypt.init_app(app)

# QRCode
qrcode = QRcode()
qrcode.init_app(app)

# Babel
domain = Domain(dirname='translations')
babel = Babel(default_domain=domain)
babel.init_app(app)

# Flask-Assets
from .assets import bundles
assets = Environment(app)
assets.append_path(os.path.join(os.path.dirname(__file__), './static'))
assets.append_path(os.path.join(os.path.dirname(__file__), './static/bower_components'))
assets.register(bundles)

# Flask-Admin
admin = Admin(app, name='Interface Admin', index_view=StatisticsView(url='/admin', name='Vue générale'))
admin.add_view(CompanyView(get_db().companies, name='Entreprises'))
admin.add_view(UserView(get_db().users, name='Utilisateurs'))
admin.add_view(JobView(get_db().jobs, name='Offres'))
admin.add_view(StreamView(get_db().stream, name='Stream'))
admin.add_link(MenuLink(name='Se déconnecter', url='/deconnexion'))

# SSLify
with app.app_context():
    sslify = SSLify()
    sslify.init_app(app)

# CDN
cdn = CDN()
cdn.init_app(app)

# S3 client
s3_client = boto3.client('s3')

# Blueprints
from .views import bp as bp_main
app.register_blueprint(bp_main)
from .users.views import bp as bp_users
app.register_blueprint(bp_users, url_prefix='/candidats')
from .companies.views import bp as bp_companies
app.register_blueprint(bp_companies, url_prefix='/recruteurs')

# Init
from . import helpers, login, storage
from .admin import helpers
from .companies import helpers
from .users import helpers
