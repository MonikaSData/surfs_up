# Import dependency
from flask import Flask
# Create a new Flask instance
app = Flask(__name__)
# Create Flask Route
@app1.route('/')
def hello_world():
    return 'Hello world!'