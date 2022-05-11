# This contain unit test case for config for my application in each environment.


def test_development_config(application):
    application.config.from_object('app.config.DevelopmentConfig')

    assert application.config['DEBUG']
    assert not application.config['TESTING']