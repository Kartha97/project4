"""Test the csv songs upload"""
"""csv file upload test"""
import os
from app.transactions.forms import csv_upload
import csv
from app.db.models import User
from app import db


def test_csv(application, client):
    res = client.get("/transactions/upload")
    print(res.data)
    assert res.status_code == 302

