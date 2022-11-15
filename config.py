import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from models import Base

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{'/Users/adomin/Documents/Python/Flask_API/widgets.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Base.metadata.create_all(engine)

db = SQLAlchemy(app)
ma = Marshmallow(app)