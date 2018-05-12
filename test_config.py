"""
test_config: configuration file
"""
DEGUB = True
SECRET_KEY = 'your-secret-key'
USERNAME = 'admin'
invalid_key = 'hello' # lowercase key not loaded.

from flask import Flask
app = Flask(__name__)
app.config.from_object('test_config')
    # load all uppercase variables
    # from Python module 'test_config.py' into app.config

print(app.config['DEBUG'])
print(app.debug)                    # Proxy to 'DEBUG'
print(app.config['SECRET_KEY'])
print(app.secret_key)
print(app.config['USERNAME'])
# print(app.username)               # No proxy for 'USERNAME'
print(app.config['invalid_key'])  # lower key not loaded
