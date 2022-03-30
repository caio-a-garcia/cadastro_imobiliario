#! python3
# cadastro_imobiliario/__init__.py

from .model import Imovel, Individuo, Aluguel
from hashlib import sha512
from getpass import getpass
from pprint import pprint

imoveis = []
inquilinos = []
proprietarios = []
alugueis = []

def login():
    usuario = 'caio.crud'
    senha_hash = '40e881f982258765b507b41a0d73f44bb94bf408f6fe9d3e82d3b8ae904cdd860e3656db6a083664f6d8ea6d0d5c58b3079835c8ae95a19010f8dbc28c19b6c0'

    tentativa_usuario = input('Usuario: ')
    tentativa_senha = getpass('Senha: ')
    tent_senha_hash = sha512(tentativa_senha.encode()).hexdigest()
    autenticado = usuario == tentativa_usuario and senha_hash == tent_senha_hash

    return autenticado


def cadastro(tipo):
    
    def cadastrar_imovel():
        cep = input('CEP: ')
        cidade = input('Cidade: ')
        bairro = input('Bairro: ')
        logradouro = input('Logradouro: ')
        id = len(imoveis)
        return Imovel(logradouro, cep, bairro, cidade, id)

    def cadastrar_individuo(grupo):
        nome = input('Nome: ')
        nascimento = input('Data de nascimento: ')
        id = len(grupo)
        return Individuo(nome, nascimento, id)

#    def cadastrar_aluguel():
        

    if tipo == 'imovel':
        imovel = cadastrar_imovel()
        imoveis.append(imovel.resumo())
    elif tipo == 'inquilino':
        inquilino = cadastrar_individuo(inquilinos)
        inquilinos.append(inquilino.resumo())
    elif tipo == 'proprietario':
        proprietario = cadastrar_individuo(proprietarios)
        proprietarios.append(proprietario.resumo())
    elif tipo == 'aluguel':
        print('Cadastro de aluguel ainda nao implementado')
    else:
        raise ValueError('Argumento nao suportado por funcao cadastro(tipo)')


def menu_cadastro():
    enunciado = '''
O que voce gostaria de cadastrar: 
1) Imovel
2) Inquilino
3) Proprietario
4) Aluguel
0) Sair
'''
    tipo_cadastro = ''
    sair = 0
    repetir = ''

    while True:
        opcao = input(enunciado)
        if opcao == '0':
            sair = 1
            break
        elif opcao == '1':
            tipo_cadastro = 'imovel'
        elif opcao == '2':
            tipo_cadastro = 'inquilino'
        elif opcao == '3':
            tipo_cadastro = 'proprietario'
        elif opcao == '4':
            tipo_cadastro = 'aluguel'
        else:
            print('Opcao invalida. Selecione o numero correspondente a sua opcao.')
            continue
        break

    if sair != 1:
        cadastro(tipo_cadastro)
        repetir = input('Cadastrar mais um item? ')
    if repetir == 'Sim':
        menu_cadastro()


def menu_consulta():
    for imovel in imoveis:
        pprint(imovel)

    for inquilino in inquilinos:
        pprint(inquilino)

    for proprietario in proprietarios:
        pprint(proprietario)


def menu():
    enunciado = '''
Para escolher o que quer fazer, digite o numero relacionado a sua opcao:
1) Cadastro
2) Consulta
3) Atualizar
4) Apagar
0) Sair
'''
    
    while True:
        opcao = input(enunciado)
        if opcao == '0':
            print('Ate a proxima')
            break
        elif opcao == '1':
            menu_cadastro()
        elif opcao == '2':
            menu_consulta()
        elif opcao == '3':
            print('menu_atualizar()')
        elif opcao == '4':
            print('menu_apagar()')
        else:
            print('Favor escolher uma opcao valida.')

    print(f'Imoveis: {imoveis}, Inquilinos: {inquilinos}, Proprietarios: {proprietarios}, Alugueis: {alugueis}')
    

def start():
    while not login():
        print('Falha na autenticacao')
    print('Login bem sucedido')

    menu()

if __name__ == '__main__':
    start()
