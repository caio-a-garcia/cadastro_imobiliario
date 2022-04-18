#! python3
# cadastro_imobiliario/model.py

class Imovel:
    def __init__(self, logradouro, cep, bairro, cidade, id):
        self.logradouro = logradouro
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.id = id

    def resumo(self):
        mapa = {
            "logradouro": self.logradouro,
            "cep": self.cep,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "id": self.id,
        }
        return mapa


class Individuo:
    def __init__(self, nome, data_de_nascimento, id):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.id = id

    def resumo(self):
        mapa = {
            "nome": self.nome,
            "data_de_nascimento": self.data_de_nascimento,
            "id": self.id,
        }
        return mapa

class Aluguel:
    def __init__(self, id_imovel, id_proprietario, id):
        self.id_imovel = id_imovel
        self.id_proprietario = id_proprietario
        self.id = id

    def resumo(self):
        mapa = {
            "id imovel": self.id_imovel,
            "id proprietario": self.id_proprietario,
            "id": self.id,
        }
        return mapa

class Contrato:
    def __init__(self, id_aluguel, id_inquilino, id):
        self.id_aluguel = id_aluguel
        self.id_inquilino = id_inquilino
        self.id = id

    def resumo(self):
        mapa = {
            "id aluguel": self.id_aluguel,
            "id inquilino": self.id_inquilino,
            "id": self.id
        }
        return mapa
