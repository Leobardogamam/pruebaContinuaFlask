from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hola desde el directorio principal')


@app.route("/hola/<nombre>", methods=['GET','POST'])
def hello(nombre):
    return jsonify(message=f'Hello from path! {nombre}')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
