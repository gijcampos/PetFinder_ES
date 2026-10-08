    versao_CRUD = "1.0"

    class Cadastro:
        #Construtor = __init__
        #this = self
        def __init__(self, nome: str, email: str, telefone: str, senha: str):
            self.nome = nome
            self.email = email
            self.telefone = telefone
            self.senha = senha