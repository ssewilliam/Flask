# -*- coding:UTF-8 -*-
"""
j2_template_inheritance:Test base and derived templates
"""
from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return render_template('j2_derived.html')

if __name__ == '__main__':
    app.run()