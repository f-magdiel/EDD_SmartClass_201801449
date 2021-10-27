from flask import Flask, request
from flask_cors import CORS
import flask

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/login')
def login():
    return {
        "miembros":["Miembro1","Miembro2","Miembro3"]
    }

app.run(host='0.0.0.0', port=3000, debug=True)