
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    #return 'Hello from Flask!'
    return render_template('-static/leader.html', name=name)