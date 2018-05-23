# -*- coding: UTF-8 -*-
"""
test_session:Test Flask's session
"""
from flask import Flask, session, render_template, url_for, g, escape, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.debug = True

@app.before_request
def before_request():
    g.start_time = time.time() #store in g for this request and this user onlya

@app.teardown_request
def teardown_request(exception=None):
    time_taken = time.time - g.start_time # Retrieve from g
    print (time_taken)
@app.route('/')
def main():
    if 'username' in session:
        return "You are already logged in as %s " % escape(session['username'])
            # Escape special html characters to prevent XSS
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    # For sub post requests
    if request.method == "POST":
        username = request.form['username']
        session['username'] = username
        return "Login as %s" % escape(username)
    
    # for initial get request
    return '''
        <form method="POST">
            <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
        '''
@app.route('/logout')
def logout():
    # remove 'username' from session if it exists
    session.pop('username',None)
    return redirect(url_for('main'))
if __name__ == '__main__':
    app.run()
