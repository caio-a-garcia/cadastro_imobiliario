#! python3
# cadastro_imobiliario/model.py

from secrets import choice
from string import ascii_letters, digits

def generateID():
    return ''.join(choice(ascii_letters + digits) for _ in range(16))

class Imovel():
    def __init__(self, logradouro, cep, bairro, cidade):
        self.logradouro = logradouro
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.id = generateID()


class Individuo():
    def __init__(self, nome, data_de_nascimento):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.id = generateID()


class Aluguel():
    def __init__(self, imovel, inquilino, proprietario):
        self.imovel = imovel
        self.inquilino = inquilino
        self.proprietario = proprietario
        self.id = generateID()
