usuarios = [['ryancliente','cliente123']]
adm = [['ryanadm','adm123']]

def menulogin():
    print('-----Menu de login-----')
    print('0-Finalizar')
    print('1-Fazer login como usuário')
    print('2-Fazer login como administrador')
    print('-----------------------')
    op = int(input('Digite a opção desejada: '))
    return op

def confirmar(login, senha):
    confirm = []
    confirm.insert(0, [login, senha])
    if confirm[0] in usuarios and (len(login.strip()) != 0 and len(senha.strip()) != 0):
        return True
    else:
        return False

def criar():
    while True:
        login = input('Login: ')
        senha = input('Senha: ')
        confirm = []
        confirm.insert(0, [login, senha])
        if confirm[0] not in usuarios and (len(login.strip()) != 0 and len(senha.strip()) != 0):
            usuarios.insert(0, [login, senha])
            print(f'Conta criada, seja bem vindo {login}')
            break
        else:
            print('Login existente ou inválido, tente outro')

def menu_usuario():
    print('---Menu Principal---')
    print('1-Produtos a venda')
    print('2-Agendar serviços')
    print('0-Sair')
    print('--------------------')
    op = int(input('O que deseja: '))
    return op