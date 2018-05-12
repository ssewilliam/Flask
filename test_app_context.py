import unittest
from flask import request

class MyTest(unittest.TestCase):
    def test_something(self):
        with app.test_request_contest('/?name=peter'):
            # create a request object which is needed to pass the url parameter to the request object
            # The with statement automatically pushes on entry
            # You can now view attributes on the request context stac by using 'request'
            assert flask.request.path == '/'
            assert flask.request.args['name'] =='peter'
            # the with statement automatically pops on exit
        # after the with statement the request context stack is empty

