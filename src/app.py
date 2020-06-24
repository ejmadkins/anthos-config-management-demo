from flask import Flask
from flask import render_template
import requests
 
app = Flask(__name__)

@app.route('/')
def t_rex_runner():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)