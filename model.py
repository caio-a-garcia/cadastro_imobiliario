#! python3
# cadastro_imobiliario/model.py

from secrets import choice
from string import ascii_letters, digits


def generateID():
    return "".join(choice(ascii_letters + digits) for _ in range(16))


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


# class Aluguel:
#     def __init__(self, imovel_id, inquilino, proprietario, id):
#         self.imovel = imovel_id
#         self.inquilino_id = inquilino.id
#         self.proprietario_id = proprietario.id
#         self.id = id

#     def resumo_ids(self):
#         mapa = {
#             "imovel": self.imovel,
#             "inquilino": self.inquilino_id,
#             "proprietario": self.proprietario_id,
#             "aluguel_id": self.id,
#         }
