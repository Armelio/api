from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!' 

CORS(app)

if __name__ == '__main__':
    app.run()