from flask import Flask
from flask import render_template
import requests
import os
 
app = Flask(__name__)

CLOUD_ENV=os.environ.get('environment')

@app.route('/')
def t_rex_runner():
    return render_template('index.html', CLOUD_ENV=CLOUD_ENV)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)