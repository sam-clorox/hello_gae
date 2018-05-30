from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
  return "I am strong enough"

@app.route('/hello')
def hello():
  return "Hello... I am here"

