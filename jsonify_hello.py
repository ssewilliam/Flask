"""
jsonify_hello: Test Json response
"""
from flask import Flask, jsonify, render_template
app = Flask(__name__)
app.debug = True

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404     # Not Found

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500     # Internal server error

@app.route('/a')
def a():
    return jsonify({'message': 'unknown user'}),400
    # response.data is
    # {
    #   "message": "unknown user"
    # }

@app.route('/b')
def b():
    return jsonify(username='peter', id =123),200
    # response.data is
    # {        
    #   "id": 123
    #    "username": "peter"
    # }

if __name__ == '__main__':
    app.run()        