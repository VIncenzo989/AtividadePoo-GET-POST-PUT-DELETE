from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
alunos_bd = []

@app.route("/alunos", methods=["GET"])
def retornarAlunos():
    return jsonify(alunos_bd)

@app.route("/alunos", methods=["POST"])
def salvarAlunos():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    idade = dados.get("idade")
    curso = dados.get("curso")
    aluno = {"id": id, "nome": nome, "idade": idade, "curso": curso}
    alunos_bd.append(aluno)
    return jsonify(aluno)

@app.route("/alunos/<int:id>", methods=["PUT"])
def editarAlunos(id):
    dados = request.get_json()
    nome = dados.get("nome")
    idade = dados.get("idade")
    curso = dados.get("curso")
    for aluno in alunos_bd:
        if aluno["id"] == id:
           aluno["nome"] = nome
           aluno["curso"] = curso
           aluno["idade"] = idade
           return jsonify(aluno), 200

    return jsonify({"erro": "aluno não encontrado"}), 404

@app.route("/alunos/<int:id>", methods = ["DELETE"])
def removerAlunos(id):
    for aluno in alunos_bd:
        if aluno["id"] == id:
            alunos_bd.remove(aluno)
        return "", 204
    
    return jsonify({"erro": "aluno não encontrado"}), 404

app.run(debug=True)