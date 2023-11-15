
class Funcionarios:
    def __init__(self, matricula, nome, cargo, nome_usuario, senha, data_atual, hora_atual, status, sincronizado) -> None:
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.data_atual = data_atual
        self.hora_atual = hora_atual
        self.status = status
        self.sincronizado = sincronizado


class Estoque:
    def __init__(self, cod, nome, descricao, quantidade, preco_compra, preco_venda, data_atual, hora_atual, status, sincronizado) -> None:
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


class Vendas:
    def __init__(self, id, nome, quantidade, valor, total, data, hora, status, sincronizado) -> None:
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.total = total
        self.data = data
        self.hora = hora
        self.status = status
        self.sincronizado = sincronizado
