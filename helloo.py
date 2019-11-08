# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:42:08 2019

@author: adjimagnan
"""

from flask import Flask, render_template
app=Flask(__name__)
app.config['DEBUG'] = True
#==============================================================================
# @app.route('/')
# def index():
#     return  '<h1>Hello World<h1>'
#==============================================================================
@app.route('/')    
def scraptfile():
    fl = open('example.txt')
    return render_template('index.html', fl)    
if __name__ == '__main__':
    app.run()
