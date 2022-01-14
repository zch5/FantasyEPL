from flask import Flask
from models import db
import os

app = Flask(__name__)
app.config.update(dict(
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default',

	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
))

db.init_app(app)

@app.cli.command('initdb')
def initdb_command():
    # Creates the database tables
    db.create_all()
    print('Initialized the database.')