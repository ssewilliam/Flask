# -*- coding:UTF-8 -*-
"""
test_contextvar:Defining variables for all views
"""

from flask import Flask, render_template, session
app = Flask(__name__)

@app.context_processor
def temlate_context():
    '''Return a dictionary of key-value pairs,
    which will be available to all views in the context'''

    if 'username' in session:
        username = session['username']
    else:
        username = 'peter'
    
    return {'version':88, 'username':username}
@app.route('/')
def main():
    return render_template('test_contextvar.html')

if __name__ == '__main__':
    app.run(debug = True)