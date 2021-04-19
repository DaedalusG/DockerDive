from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
    return '666-69-7'
