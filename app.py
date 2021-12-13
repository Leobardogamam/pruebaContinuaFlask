from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

allUser = [{"id":0,"nombre":"Leobardo"}, {"id":1,"nombre":"Ricardo"}]

@app.route('/')
def inicio():
    return "Hola amigo :)"

@app.route('/app/<id>', methods=["GET"])
def users_actions(id):
    return jsonify(allUser[int(id)])

@app.route('/app/v1/users', methods=["POST","GET"])
def users_actions2():
    if(request.method == "GET"):
        return jsonify(allUser)
    else:
        user = {"id": request.form["id"], "nombre": request.form["nombre"]}
        allUser.append(user)
        return jsonify(user)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
