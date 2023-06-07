import os
import sys

from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={'/*', '*'})

@app.route('/')
def index():
    return render_template('index.html', paths=(p for p in os.listdir('static') if p.endswith('.pdf')))

@app.route('/view/<path>')
def view(path):
    return render_template('view.html', path=path)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 2011
    else:
        port = int(sys.argv[1])
    app.run(port=port, host='0.0.0.0')