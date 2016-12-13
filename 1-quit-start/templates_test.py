# -*- coding:utf-8 -*-
__author__ = 'YUN'
__date__ = 2016 / 12 / 13


from flask import render_template,Flask
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()