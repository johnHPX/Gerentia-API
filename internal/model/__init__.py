
class Funcionarios:
    def __init__(self, matricula: int = 0, nome: str = "", cargo: str = "", nome_usuario: str = "", senha: str = "", data_atual: str = "", hora_atual: str = "", status: int = 0, sincronizado: int = 0) -> None:
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
    def __init__(self, cod: str = "", nome: str = "", descricao: str = "", quantidade: int = 0, preco_compra: float = 0.0, preco_venda: float = 0.0, data_atual: str = "", hora_atual: str = "", status: int = 0, sincronizado: int = 0) -> None:
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
    def __init__(self, id: int = 0, nome: str = "", quantidade: int = 0, valor: int = 0, total: int = 0, data: str = "", hora: str = "", status: int = 0, sincronizado: int = 0) -> None:
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.total = total
        self.data = data
        self.hora = hora
        self.status = status
        self.sincronizado = sincronizado
