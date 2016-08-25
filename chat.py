# -*- coding: utf-8 -*-

"""
Chat Server
===========

This simple application uses WebSockets to run a primitive chat server.
"""

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
    app.run()