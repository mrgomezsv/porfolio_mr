from flask import Flask

app = Flask(__name__)

@app.route('/')
def run():
    return 'Hello World Flask'