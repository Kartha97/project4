"""Test the csv songs upload"""
"""csv file upload test"""
import os
from app.transactions.forms import csv_upload
import csv
from app.db.models import User
from app import db


def test_csv_upload_link(application, client):
    res = client.get("/transactions/upload")
    print(res.data)
    assert res.status_code == 302

def test_csv_upload(application, client):
    res = client.get("/transactions/upload")
    print(res.data)
    assert res.status_code == 302

    with application.app_context():
        user = User('test@test.com', 'test1234')
        filepath = 'tests/csvtest.csv'
        testvar = ''
        with open(filepath, encoding='utf-8-sig') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                testvar = row
            assert testvar == {'AMOUNT': '1000', 'TYPE': 'CREDIT'}


def test_csv_upload_link_submission(client):
    upload_res = client.post("/transactions/upload", data='tests/csvtest.csv', follow_redirects=True)
    assert upload_res.status_code == 200