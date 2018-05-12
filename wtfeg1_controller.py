"""
wtfeg1_controller: Flask-WTF Example 1 - app controller
"""

import os, binascii
from flask import Flask, render_template
from wtfeg1_form import LoginForm

# initialize Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24)) # FLask-WTF: Needed for CSRF
app.debug = True

@app.route('/')
def main():
    # Construct an instance of LoginForm
    _form = LoginForm()

    # render an html page with the login form instance created
    return render_template('wtfeg1_login.html',form=_form)

if __name__ == '__main__':
    app.run()