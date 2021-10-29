from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.wrappers import response

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/login', methods=['post'])
def login():
   
    usuario = request.json['usuario']
    contra = request.json['contraseña']
    if request.method=='POST':
        if usuario == "admin" and contra =="admin":
            return jsonify([{
                "tipo":usuario,
                "bandera":True
            }])

        
    
    

app.run(host='0.0.0.0', port=3000, debug=True)