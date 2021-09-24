from flask import Flask, request

#definir
app = Flask(__name__)

#rutas
@app.route('/ejemplo')
def ejemplo():
    return "ejemplo servido"

#ejecutar
app.run(host='0.0.0.0',port=3000,debug=True)
