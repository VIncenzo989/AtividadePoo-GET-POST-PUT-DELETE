from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
musicas_bd = []

@app.route("/musicas", methods=["GET"])
def retornarMusicas():
    return jsonify(musicas_bd)

@app.route("/musicas", methods=["POST"])
def salvarMusicas():
    global id
    id = id + 1
    dados = request.get.json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    artista = dados.get("artista")
    musica = {"id": id, "nome": nome, "ano": ano, "artista": artista}
    musicas_bd.append(musica)
    return jsonify(musica)

@app.route("/musicas/<int:id>", methods=["PUT"])
def editarMusicas(id):
    dados = request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    artista = dados.get("artista")
    for musica in musicas_bd:
        if musica["id"] == id:
           musica["nome"] = nome
           musica["artista"] = artista
           musica["ano"] = ano
           return jsonify(musica), 200

    return jsonify({"erro": "Musica não encontrado"}), 404

@app.route("/musicas/<int:id>", methods = ["DELETE"])
def removerMusicas(id):
    for musica in musicas_bd:
        if musica["id"] == id:
            musicas_bd.remove(musica)
        return "", 204
    
    return jsonify({"erro": "musica não encontrado"}), 404

app.run(debug=True)
