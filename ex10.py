from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
cursos_bd = []

@app.route("/cursos", methods=["GET"])
def retornarCursos():
    return jsonify(cursos_bd)

@app.route("/cursos", methods=["POST"])
def salvarCursos():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")
    curso = {"id": id, "nome": nome, "instituicao": instituicao, "duracao": duracao}
    cursos_bd.append(curso)
    return jsonify(curso)

@app.route("/cursos/<int:id>", methods=["PUT"])
def editarCursos(id):
    dados = request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")
    for curso in cursos_bd:
        if curso["id"] == id:
            curso["nome"] = nome
            curso["instituicao"] = instituicao
            curso["duracao"] = duracao
            return jsonify(curso), 200

    return jsonify({"erro": "curso não encontrado"}), 404

@app.route("/cursos/<int:id>", methods=["DELETE"])
def removerCursos(id):
    for curso in cursos_bd:
        if curso["id"] == id:
            cursos_bd.remove(curso)
            return "", 204
    
    return jsonify({"erro": "curso não encontrado"}), 404

app.run(debug=True)