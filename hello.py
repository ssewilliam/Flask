# -*- cording: UTF-8 -*-
"""
hello: First Python-Flask webapp to say hello
"""
from flask import Flask, render_template # from 'flask' module import 'Flask' class

app = Flask(__name__)   # Construct an instance of Flask class for our web app

@app.route("/")         # URL '/' to be handeled by the main() route handler
@app.route("/hello")         # URL '/' to be handeled by the main() route handler
@app.route('/hi')
def main():
    """Say hello""" 
    """Render an HTML template and return"""
    return render_template('hello.html')    

if __name__ == "__main__":  # if script is executed directly (instead of via import)
    app.run(debug=True)    # Launch the built-in webserver and run this Flask webapp