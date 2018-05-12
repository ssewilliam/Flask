# -*- coding: UTF-8 -*-
"""
hello_jinja: Getting started with jinja2 templates
"""

from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return render_template("j2_query.html")

@app.route("/process", methods=['POST'])
def process():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    _username = request.form.get('username')  #get(attr) returns none if attr is not present

    #validate and send response
    if _username:
        return render_template('j2_response.html',username=_username)
    else:
        return 'Please go back and enter your name', 400
    
if __name__ == '__main__':
    app.run()
    