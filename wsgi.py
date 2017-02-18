#!/usr/bin/env python3

'''
这个文件是给gunicorn用的
'''
import sys
from os.path import abspath
from os.path import dirname

import app

sys.path.insert(0, abspath(dirname(__file__)))


application = app.configured_app()
