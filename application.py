# application.py
 
from flask import Flask, render_template
 
 
application = Flask(__name__)
 
 
@application.route('/')
def v1():
   return 'Example app v1 updated'