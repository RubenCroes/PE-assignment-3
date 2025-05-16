import pymysql
from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config)
# This tells Flask to trust the first proxy in front of it (the ALB)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
