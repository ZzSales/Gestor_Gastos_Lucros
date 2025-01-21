def calcular_lucro():
    """
    Função para calcular o lucro total.
    :return: Lucro total calculado.
    """
    # Supondo que você tenha listas de compras e vendas armazenadas
    compras = [
        # Exemplo de dados de compras
        {'descricao': 'Produto A', 'preco': 10.0, 'quantidade': 5},
        {'descricao': 'Produto B', 'preco': 20.0, 'quantidade': 3}
    ]
    vendas = [
        # Exemplo de dados de vendas
        {'descricao': 'Produto A', 'preco': 15.0, 'quantidade': 4},
        {'descricao': 'Produto B', 'preco': 25.0, 'quantidade': 2}
    ]

    total_gasto = sum(compra['preco'] * compra['quantidade'] for compra in compras)
    total_vendido = sum(venda['preco'] * venda['quantidade'] for venda in vendas)
    lucro = total_vendido - total_gasto

    return lucro