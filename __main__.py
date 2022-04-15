#! python3
# -*- coding: latin-1 -*-
# cadastro_imobiliario/__init__.py

from model import Imovel, Individuo, Aluguel
from hashlib import sha512
from getpass import getpass
from pprint import pprint

imoveis = [{'bairro': 'Centro',
            'cep': '00000000',
            'cidade': 'Udi',
            'id': 0, 'logradouro':
            'Rua Goias'}] # TODO: tirar item colocado para dev

inquilinos = [{'data_de_nascimento': '19\\12\\1998',
               'id': 0, 'nome': 'Caio'}]

proprietarios = [{'data_de_nascimento': '13/11/1969',
                  'id': 0, 'nome': 'Augusto'}]

alugueis = []
relacao_alugueis = []

def init_count(lista):
    if len(lista) > 0:
        return int(lista[-1]['id']) + 1
    else:
        return 0


# count usado para gerar os ids de cada lista
imoveis_count = init_count(imoveis)
inquilinos_count = init_count(inquilinos)
proprietarios_count = init_count(proprietarios)
alugueis_count = init_count(alugueis)
relacao_alugueis_count = init_count(relacao_alugueis)

def login():
    usuario = 'caio.crud'
    senha_hash = '40e881f982258765b507b41a0d73f44bb94bf408f6fe9d3e82d3b8ae904cdd860e3656db6a083664f6d8ea6d0d5c58b3079835c8ae95a19010f8dbc28c19b6c0'

    tentativa_usuario = input('Usu�rio: ')
    tentativa_senha = getpass('Senha: ')
    tent_senha_hash = sha512(tentativa_senha.encode()).hexdigest()
    autenticado = usuario == tentativa_usuario and senha_hash == tent_senha_hash

    return autenticado


def inteiro_ou_falso(valor):
    if valor.isdigit():
        return valor
    else:
        return False

def buscar_id_na_lista(lista, ID):
    for item in lista:
        if item['id'] == int(ID):
            return item
    return False

def consultar_por_id(lista, ID):
    valor = inteiro_ou_falso(ID)
    if valor:
        pprint(buscar_id_na_lista(lista, ID))
    else:
        print('ID deve ser um n�mero inteiro')


        
def cadastro(tipo):
    
    def cadastrar_imovel():
        cep = input('CEP: ')
        cidade = input('Cidade: ')
        bairro = input('Bairro: ')
        logradouro = input('Logradouro: ')
        global imoveis_count
        id = imoveis_count
        imoveis_count += 1
        return Imovel(logradouro, cep, bairro, cidade, id)

    
    def cadastrar_individuo(grupo):
        nome = input('Nome: ')
        nascimento = input('Data de nascimento: ')
        if grupo == inquilinos:
            global inquilinos_count
            id = inquilinos_count
            inquilinos_count += 1
        elif grupo == proprietarios:
            global proprietarios_count
            id = proprietarios_count
            proprietarios_count += 1
        
        return Individuo(nome, nascimento, id)

    
    def cadastrar_aluguel(): 
        print('Para descobrir os IDs de inquilino(s) e propriet�rio relevantes, use a fun��o consulta')
        id_imovel = -1
        id_proprietario = -1
        
        while True:
            id_imovel = input('Digite o id do im�vel alugado: ')
            consultar_por_id(imoveis, id_imovel)
            if not inteiro_ou_falso(id_imovel):
                continue
            confirma_imovel = input('O im�vel acima � o correto [s/n]: ')
            if confirma_imovel in ['s', 'S', 'sim', 'Sim']:
                break

        while True:
            id_proprietario = input('Digite o id do proprietario do im�vel: ')
            consultar_por_id(proprietarios, id_proprietario)
            if not inteiro_ou_falso(id_proprietario):
                continue
            confirma_proprietario = input('O proprietario acima � o correto [s/n]: ')
            if confirma_proprietario in ['s', 'S', 'sim', 'Sim']:
                break

        global alugueis_count
        id_aluguel = alugueis_count
        alugueis_count += 1
        return Aluguel(id_imovel, id_proprietario, id_aluguel)
        

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
        aluguel = cadastrar_aluguel()
        alugueis.append(aluguel.resumo())
    else:
        raise ValueError('Argumento n�o suportado por fun��o cadastro()')


def menu_cadastro():
    enunciado = '''
O que voc� gostaria de cadastrar: 
1) Im�vel
2) Inquilino
3) Propriet�rio
4) Aluguel
0) Sair

'''
    tipo_cadastro = ''
    continuar = True
    repetir = ''

    while True:
        opcao = input(enunciado)
        if opcao == '0':
            continuar = False
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
            print('Op��o inv�lida. Selecione o n�mero correspondente � sua op��o.')
            continue
        break

    if continuar:
        cadastro(tipo_cadastro)
        repetir = input('Cadastrar mais um item? ')
    if repetir in ['Sim', 'sim', 'S', 's', 'Yes', 'yes', 'Y', 'y']:
        menu_cadastro()


def menu_consulta():
    enunciado_consulta = '''
O que voc� gostaria de consultar:
1) Im�veis
2) Inquilinos
3) Propriet�rios
4) Alugu�is
0) Sair
'''
    
    enunciado_campo = '''
Qual o campo a ser pesquisado:
1) Mostrar todos'''

    campos_imovel = '''2) ID
3) CEP
4) Cidade
5) Bairro
6) Logradouro
0) Sair
'''

    campos_individuo = '''2) ID
3) Nome
4) Data de Nascimento
0) Sair
'''

    campos_aluguel = '2) ID\n'
    
    def consultar_item(lista, campo, valor):
        for item in lista:
            if item[campo] == valor:
                pprint(item)

    def consultar_imoveis():
        print('Im�veis: ')
        for imovel in imoveis:
            pprint(imovel)

    def consultar_inquilinos():
        print('Inquilinos: ')
        for inquilino in inquilinos:
            pprint(inquilino)

    def consultar_proprietarios():
        print('Propriet�rios: ')
        for proprietario in proprietarios:
            pprint(proprietario)

    def consultar_alugueis():
        print('Alugu�is: ')
        for aluguel in alugueis:
            print('Aluguel eh tipo ' + str(type(aluguel)))
            imovel = buscar_id_na_lista(imoveis, aluguel['id imovel'])
            proprietario = buscar_id_na_lista(proprietarios, aluguel['id proprietario'])
            endereco = ', '.join((imovel['logradouro'], imovel['cidade']))
            mapa = {
                'id': aluguel['id'],
                'id proprietario': aluguel['id proprietario'],
                'proprietario': proprietario['nome'],
                'id imovel': imovel['id'],
                'endere�o': endereco,
            }

            pprint(mapa)
                

    def consultar_tudo():
        consultar_imoveis()
        consultar_inquilinos()
        consultar_proprietarios()
        consultar_alugueis()
        

    def menu_imoveis():
        campo = ''
        print(enunciado_campo)
        opcao = input(campos_imovel)
        while True:
            if opcao == '0':
                break
            elif opcao == '1':
                consultar_imoveis()
                break
            else:
                if opcao == '2':
                    campo = 'id'
                elif opcao == '3':
                    campo = 'cep'
                elif opcao == '4':
                    campo = 'cidade'
                elif opcao == '5':
                    campo = 'bairro'
                elif opcao == '6':
                    campo = 'logradouro'
                else:
                    print('Op��o inv�lida. Selecione o n�mero correspondente � sua op��o.\n')
                    continue
                valor = input(f'Qual o valor de {campo} a ser procurado: ')
                if campo == 'id':
                    consultar_por_id(imoveis, valor)
                else:
                    consultar_item(imoveis, campo, valor)
                break

    def menu_inquilinos():
        campo = ''
        print(enunciado_campo)
        opcao = input(campos_individuo)
        while True:
            if opcao == '0':
                break
            elif opcao == '1':
                consultar_inquilinos()
                break
            else:
                if opcao == '2':
                    campo = 'id'
                elif opcao == '3':
                    campo = 'nome'
                elif opcao == '4':
                    campo = 'data_de_nascimento'
                else:
                    print('Op��o inv�lida. Selecione o n�mero correspondente � sua op��o.')
                    continue
                valor = input(f'Qual o valor de {campo} a ser procurado: ')
                if campo == 'id':
                    consultar_por_id(inquilinos,valor)
                else:
                    consultar_item(inquilinos, campo, valor)
                break

    def menu_proprietarios():
        campo = ''
        print(enunciado_campo)
        opcao = input(campos_individuo)
        while True:
            if opcao == '0':
                break
            elif opcao == '1':
                consultar_proprietarios()
                break
            else:
                if opcao == '2':
                    campo = 'id'
                elif opcao == '3':
                    campo = 'nome'
                elif opcao == '4':
                    campo = 'data_de_nascimento'
                else:
                    print('Op��o inv�lida. Selecione o n�mero correspondente � sua op��o.')
                    continue
                valor = input(f'Qual o valor de {campo} a ser procurado: ')
                if campo == 'id':
                    consultar_por_id(proprietarios, valor)
                else:
                    consultar_item(proprietarios, campo, valor)
                break

    
    def menu_alugueis():
        print(enunciado_campo)
        opcao = input(campos_aluguel)
        while True:
            if opcao == '0':
                break
            elif opcao == '1':
                consultar_alugueis()
                break
            if opcao == '2':
                valor = input(f'Qual o id a ser procurado: \n')
                consultar_por_id(proprietarios, valor)
                break
            else:
                print('Op��o inv�lida. Selecione o n�mero correspondente � sua op��o.')
        
    while True:
        opcao = input(enunciado_consulta)
        if opcao == '0':
            break
        elif opcao == '1':
            menu_imoveis()
        elif opcao == '2':
            menu_inquilinos()
        elif opcao == '3':
            menu_proprietarios()
        elif opcao == '4':
            menu_alugueis()
        else:
            print('Favor escolher uma op��o v�lida.')
            continue
        break


def menu_apagar():
    enunciado_apagar = '''Qual tipo de entrada voc� gostaria de apagar:
1) Im�veis
2) Inquilinos
3) Propriet�rios
4) Alugu�is
0) Sair
'''

    lista = ''

    while True:
        opcao = input(enunciado_apagar)
        if opcao == '0':
            break
        else:
            if opcao == '1':
                lista = imoveis
            elif opcao == '2':
                lista = inquilinos
            elif opcao == '3':
                lista = proprietarios
            elif opcao == '4':
                lista = alugueis
            else:
                print('Op��o inv�lida. Selecione o n�mero correspondente � sua op��o.')
                continue
            break

    if lista:
        while True:
            busca = input('''
Digite o id do item a ser exclu�do
Enter sem input para sair
''')
            if busca == '':
                break
            valor = inteiro_ou_falso(busca)
            if not valor:
                print('Favor passar um valor v�lido')
                continue
            consultar_por_id(lista, valor)
            confirma_apagar = input("Para apagar o registro acima digite 'apagar': ")
            if confirma_apagar == 'apagar':
                lista.remove(buscar_id_na_lista(lista, valor))
                print(f'Item de id == {valor} exclu�do')


def menu_atualizar():
    enunciado_atualizar = '''Qual tipo de entrada voc� gostaria de aualizar:
1) Im�veis
2) Inquilinos
3) Propriet�rios
4) Alugu�is
0) Sair
'''

    lista = ''

    while True:
        opcao = input(enunciado_atualizar)
        if opcao == '0':
            break
        else:
            if opcao == '1':
                lista = imoveis
            elif opcao == '2':
                lista = inquilinos
            elif opcao == '3':
                lista = proprietarios
            elif opcao == '4':
                lista = alugueis
            else:
                print('Op��o inv�lida. Selecione o n�mero correspondente � sua op��o.')
                continue
            break

    if lista:
        while True:
            busca = input('''
Digite o id do item a ser atualizado
Enter sem input para sair
''')

            if busca == '':
                break

            valor = inteiro_ou_falso(busca)
            if not valor:
                print('Favor passar um valor v�lido')
                continue
            consultar_por_id(lista, valor)
            # TODO: usar valor:id para achar item na lista
            while True:
                campo = input('''Qual o campo a ser atualizado?
Enter sem input para sair:
''')

                if campo == '':
                    break
                if not campo in lista:
                    print('Favor escolher um campo v�lido')
                    continue
                else:
                    novo_valor = input('Qual o novo valor do campo: ')
                    
            # TODO: terminar menu_atualizar()

def menu():
    enunciado = '''
Para escolher o que quer fazer, digite o n�mero relacionado a sua op��o:
1) Cadastro
2) Consulta
3) Atualizar
4) Apagar
0) Sair
'''
    
    while True:
        opcao = input(enunciado)
        if opcao == '0':
            print('At� a pr�xima')
            break
        elif opcao == '1':
            menu_cadastro()
        elif opcao == '2':
            menu_consulta()
        elif opcao == '3':
            print('menu_atualizar()')
        elif opcao == '4':
            menu_apagar()
        else:
            print('Favor escolher uma opcao valida.')
    

def start():
    # while not login():
    #     print('Falha na autentica��o')
    # print('Login bem sucedido')
    # TODO: ativar login
    menu()

if __name__ == '__main__':
    start()
