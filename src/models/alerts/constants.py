"""
Sample code of sending emails via mailgun:
(from https://www.mailgun.com)
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
        data={"from": "Excited User <excited@samples.mailgun.org>",
              "to": ["devs@mailgun.net"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})
"""
import os


# use sand box of mailgun for testing
# the three constants are serviced on Heroku
# URL = os.environ.get('MAILGUN_URL')
# API_KEY = os.environ.get('MAILGUN_API_KEY')
# FROM = os.environ.get('MAILGUN_FORM')

# use sand box of mailgun for testing
URL = "https://api.mailgun.net/v3/sandbox97e668276aa54ee3a720cf8cdfd5e084.mailgun.org/messages"
API_KEY = "key-7532da4be110d4f55405be159b38db39"
FROM = "Mailgun Sandbox <postmaster@sandbox97e668276aa54ee3a720cf8cdfd5e084.mailgun.org>"

ALERT_TIMEOUT = 10  # 10 minutes

COLLECTION = "alerts"