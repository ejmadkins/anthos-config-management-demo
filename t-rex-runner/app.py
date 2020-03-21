from flask import Flask
from flask import render_template
import requests
 
app = Flask(__name__)

@app.route('/')
def t_rex_runner():
    return render_template('index.html', instance_id=get_zone_metadata())

def get_zone_metadata():
    return requests.get("http://metadata/computeMetadata/v1/instance/id",
        headers={'Metadata-Flavor': 'Google'}).text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')