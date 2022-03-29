#! python3
# cadastro_imobiliario/__init__.py

# import model
from hashlib import sha512
from getpass import getpass

def login():
    usuario = 'caio.crud'
    senha_hash = '40e881f982258765b507b41a0d73f44bb94bf408f6fe9d3e82d3b8ae904cdd860e3656db6a083664f6d8ea6d0d5c58b3079835c8ae95a19010f8dbc28c19b6c0'

    tentativa_usuario = input('Usuario: ')
    tentativa_senha = getpass('Senha: ')
    tent_senha_hash = sha512(tentativa_senha.encode()).hexdigest()
    autenticado = usuario == tentativa_usuario and senha_hash == tent_senha_hash

    return autenticado

def menu():
    enunciado = '''Para escolher o que quer fazer, digite o numero relacionado a sua opcao:
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
            print('menu_cadastro()')
        elif opcao == '2':
            print('menu_consulta()')
        elif opcao == '3':
            print('menu_atualizar()')
        elif opcao == '4':
            print('menu_apagar()')
        else:
            print('Favor escolher uma opcao valida.')
    
    

def start():
    imoveis = []
    inquilinos = []
    proprietarios = []
    alugueis = []

    while not login():
        print('Falha na autenticacao')
    print('Login bem sucedido')

    menu()

if __name__ == '__main__':
    start()
