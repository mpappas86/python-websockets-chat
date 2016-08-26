# -*- coding: utf-8 -*-

import os
import logging
import gevent
from flask import Flask, render_template

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
