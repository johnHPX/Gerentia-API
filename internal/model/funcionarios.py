class Funcionarios:
    def __init__(self, matricula=0, nome="", cargo="", nome_usuario="", senha="", data_atual="", hora_atual="", status=0, sincronizado=0) -> None:
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.data_atual = data_atual
        self.hora_atual = hora_atual
        self.status = status
        self.sincronizado = sincronizado
