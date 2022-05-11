import logging

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




