import os

__author__ = 'liyu'

# use sand box of mailgun for testing
# the three constants are serviced on Heroku
URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FORM')


ALERT_TIMEOUT = 10  # 10 minutes

COLLECTION = "alerts"
