"""
wtfeg2_controller: Flask-WTF Example 2 - Processing the Login Form
"""

import os, binascii
from flask import Flask, render_template, flash, url_for, redirect
from wtfeg2_form import LoginForm

# initialize the app
app = Flask(__name__)
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24)) # Flask-wtf Needed for CSRF
app.debug = True

@app.route('/', methods=['get','post'])
def main():
    form = LoginForm() # create an instance of loginform

    if form.validate_on_submit(): # post request with valid input
        # verify username and password
        if form.username.data == 'peter' and form.passwd.data == 'xxxx':
            return redirect(url_for('startapp'))
        else:
            flash('wrong username or password')
    # for the initial get request and subsequent invalid post requests
    # render the login page with the form instance created
    return render_template('wtfeg2_login.html', form=form)

@app.route('/startapp')
def startapp():
    return "The app starts here"

if __name__ == '__main__':
    app.run()
