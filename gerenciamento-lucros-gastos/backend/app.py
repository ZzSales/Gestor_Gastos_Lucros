from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Compra, Gasto, Venda
from services import calcular_lucro

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir requisições de diferentes origens

@app.route('/adicionar_compra', methods=['POST'])
def adicionar_compra():
    """
    Rota para adicionar uma nova compra.
    Espera um JSON com 'descricao', 'preco' e 'quantidade'.
    """
    data = request.json
    compra = Compra(data['descricao'], data['preco'], data['quantidade'])
    # Lógica para armazenar a compra
    return jsonify({'message': 'Compra adicionada com sucesso'}), 201

@app.route('/adicionar_gasto', methods=['POST'])
def adicionar_gasto():
    """
    Rota para adicionar um novo gasto.
    Espera um JSON com 'descricao' e 'valor'.
    """
    data = request.json
    gasto = Gasto(data['descricao'], data['valor'])
    # Lógica para armazenar o gasto
    return jsonify({'message': 'Gasto adicionado com sucesso'}), 201

@app.route('/adicionar_venda', methods=['POST'])
def adicionar_venda():
    """
    Rota para adicionar uma nova venda.
    Espera um JSON com 'descricao', 'preco_venda' e 'quantidade_vendida'.
    """
    data = request.json
    venda = Venda(data['descricao'], data['preco_venda'], data['quantidade_vendida'])
    # Lógica para armazenar a venda
    return jsonify({'message': 'Venda adicionada com sucesso'}), 201

@app.route('/calcular_lucro', methods=['GET'])
def calcular_lucro_total():
    """
    Rota para calcular o lucro total.
    Retorna um JSON com 'lucro_total'.
    """
    lucro = calcular_lucro()
    return jsonify({'lucro_total': lucro}), 200

if __name__ == '__main__':
    app.run(debug=True)