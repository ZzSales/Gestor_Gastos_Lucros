from flask import Blueprint, request, jsonify
from backend.services import calcular_lucro, adicionar_compra, adicionar_gasto

bp = Blueprint('routes', __name__)

@bp.route('/adicionar_compra', methods=['POST'])
def route_adicionar_compra():
    data = request.json
    resultado = adicionar_compra(data['preco'], data['quantidade'])
    return jsonify(resultado), 201

@bp.route('/adicionar_gasto', methods=['POST'])
def route_adicionar_gasto():
    data = request.json
    resultado = adicionar_gasto(data['valor'])
    return jsonify(resultado), 201

@bp.route('/calcular_lucro', methods=['GET'])
def route_calcular_lucro():
    lucro_total = calcular_lucro()
    return jsonify({'lucro_total': lucro_total}), 200