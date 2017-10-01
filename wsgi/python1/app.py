import os
from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'p1: Hello, World!'

@app.route('/hi')
def hi_world():
    return 'p1: Hi, World!'

class CtxRootMiddleWare(object):
    def __init__(self, app, ctx_root=''):
        self.app = app
        self.ctx_root = ctx_root

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.ctx_root):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.ctx_root):]
            environ['SCRIPT_NAME'] = self.ctx_root
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url is not part of the app.".encode()]

app.wsgi_app = CtxRootMiddleWare(app.wsgi_app, '/p1')
