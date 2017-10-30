#KEY = postgresql-closed-81267
import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
lo
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class So(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    release = db.Column(db.String(100), unique=True)
    nodename = db.Column(db.String(100), unique=True)
    kernelv = db.Column(db.String(100), unique=True)
    machine = db.Column(db.String(100), unique=True)
    processor = db.Column(db.String(100), unique=True)
    so = db.Column(db.String(100), unique=True)
    hardware = db.Column(db.String(100), unique=True)

    def __init__(self, release, nodename, kernelv, machine, processor, os, hardware):
        self.release = release
        self.nodename = nodename
        self.kernelv = kernelv
        self.machine = machine
        self.processor = processor
        self.os = os
        self.hardware = hardware

    def __repr__(self):
        return '<Name %r>' % self.os


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/so/show')
def soShow():
    so = So.query.all()
    return render_template('so.html',so = so)


@app.route('/mem/show')
def memShow():
    careers = So.query.all()
    return render_template('mem.html',carreras = careers)


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
