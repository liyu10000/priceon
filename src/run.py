'''
Project: Price of an item in a web-store for a user under a price limit
1. Creates an alert
2. Gives us an email
3. Gives us a price and item URL
4. We check the price
5. If the price is < limit
6. Notify the user through email
Repeat every 10 minutes

Models:
1. Alert
Email, Price limit, Item
2. Web-store
How to check item's price?
3. Users
Emails for notifications
Name/password/username?

Item:
Name, Price, URL
'''

from src.app import app

app.run(port=4995, debug=app.config['DEBUG'])
