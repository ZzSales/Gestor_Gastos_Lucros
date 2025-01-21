class Compra:
    def __init__(self, descricao, valor, quantidade):
        """
        Classe para representar uma compra.
        :param descricao: Descrição do item comprado.
        :param valor: Valor unitário do item.
        :param quantidade: Quantidade comprada.
        """
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade

class Gasto:
    def __init__(self, descricao, valor):
        """
        Classe para representar um gasto.
        :param descricao: Descrição do gasto.
        :param valor: Valor do gasto.
        """
        self.descricao = descricao
        self.valor = valor

class Venda:
    def __init__(self, descricao, preco_venda, quantidade_vendida):
        """
        Classe para representar uma venda.
        :param descricao: Descrição do item vendido.
        :param preco_venda: Preço unitário de venda do item.
        :param quantidade_vendida: Quantidade vendida.
        """
        self.descricao = descricao
        self.preco_venda = preco_venda
        self.quantidade_vendida = quantidade_vendida