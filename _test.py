class Erro_Database(Exception):
    def __init__(self, mensagem="Ocorreu um erro no banco de dados"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# Exemplo de uso
def minha_funcao(row):
    if row != 1:
        raise Exception(101, "Este registro não existe")
    
    return True


if __name__ == "__main__":
    # Testando a exceção personalizada
    try:
        resultado = minha_funcao(-5)
    except Exception as e:
        print(f"Exceção personalizada capturada: {e}")
        print(f"COD: {e.args[0]}")
        print(f"ERROR: {e.args[1]}")
    else:
        print(f"Resultado: {resultado}")