# -*- coding: utf-8 -*-

# flask import
from flask import render_template

# project import
from . import mod


@mod.route('/')
def index():
    return render_template('index.html')