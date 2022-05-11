import logging
import os
from app.transactions.forms import csv_upload
import csv
from app import db
from app.db.models import User, Transactions
from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transactions).count() == 0
        #showing how to add a record
        #create a record
        user = User('abc@gmail.com', 'testtest')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        #db.session.commit()
        #assert that we now have a new user
        #assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='abc@gmail.com').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'abc@gmail.com'
        #this is how you get a related record ready for insert
        user.transactions = [Transactions("CREDIT", 1000), Transactions("DEBIT",-500)]
        #commit is what saves the Transactions
        db.session.commit()
        assert db.session.query(Transactions).count() == 2
        #checking cascade delete
        db.session.delete(user)

        assert db.session.query(User).count() == 0
        assert db.session.query(Transactions).count() == 0

def test_user_initial_balance_without_any_transactions(application):
    with application.app_context():
        user = User('abc@gmail.com', 'testtest')
        db.session.add(user)
        db.session.commit()
        assert user.balance == 0
        db.session.delete(user)


def test_user_balance_after_transactions(client, application):
    with application.app_context():
        user = User('test@test.com', 'test1234')
        db.session.add(user)
        db.session.commit()
        # Checking initial balance is zero
        assert user.balance == 0
        filepath = 'tests/csvtest.csv'
        testvar = ''
        with open(filepath, encoding='utf-8-sig') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                user.balance += int(row['AMOUNT'])
                testvar = row
            # validating the data that we are uploading.
            assert testvar == {'AMOUNT': '1000', 'TYPE': 'CREDIT'}
            upload_res = client.post("/transactions/upload", data=testvar, follow_redirects=True)
            # Checking if data is being properly uploaded or not.
            assert upload_res.status_code == 200

        # Validating balance
        assert user.balance == 1000









