class Vendas:
    def __init__(self, id=0, nome="", quantidade=0, valor=0, total=0, data="", hora="", status=0, sincronizado=0) -> None:
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.total = total
        self.data = data
        self.hora = hora
        self.status = status
        self.sincronizado = sincronizado
