import os

from click.testing import CliRunner

from app.db.models import User
from app import create_database
from app.db import db

from werkzeug.security import generate_password_hash

runner = CliRunner()

def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True

def test_create_database_upload_folder():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../app/uploads')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True
