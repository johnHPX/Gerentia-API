class Estoque:
    def __init__(self, cod="", nome="", descricao="", quantidade=0, preco_compra=0.0, preco_venda=0.0, data_atual="", hora_atual="", status=0, sincronizado=0) -> None:
        self.cod = cod
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_atual = data_atual
        self.hora_atual = hora_atual
        self.status = status
        self.sincronizado = sincronizado
