# -*- coding:UTF-8 -*-
"""
hello_urlvar: Using URL variables
"""
from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/hello')
def hello():
    return 'Hello world'

@app.route('/hello/<username>') # URL with a variable
def hello_username(username):   # The function shall take the URL varable as parameter
    return 'Hello, {}'.format(username)

@app.route('/hello/<int:userid>') # Variable with type filter.Only accept int
def hello_userid(userid):
    return 'Hello, your ID id: {:d}'.format(userid)

if __name__ == '__main__':
    app.run()     # Enable reloader and debuger
        