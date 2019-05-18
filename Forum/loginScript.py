from flask import Flask, send_from_directory
import requests
from flask import request
from flask import render_template
import pafy
import vlc
import time


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('/index.html')

@app.route('/input', methods=['POST'])
def input():
    if
    
    

if __name__ == '__main__':
    app.run(debug=True)
