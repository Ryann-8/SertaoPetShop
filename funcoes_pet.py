usuarios = [['ryancliente','cliente123']]
adm = [['ryanadm','adm123']]
produtos = [["Ração para cães", "R$60", 5],["Brinquedo de borracha", "R$60", 5],["Coleira ajustável", "R$60", 5],["Shampoo para pets", "R$60", 5],["Caminha confortável", "R$60", 5]]
servicos = [["Banho e tosa", "R$100", ["Às 10H", "Às 14H"]],["Consulta veterinária", "R$100", ["Às 10H", "Às 14H"]],["Hospedagem de pets", "R$100", ["Às 10H", "Às 14H"]],["Adestramento", "R$100", ["Às 10H", "Às 14H"]],["Vacinação", "R$100", ["Às 10H", "Às 14H"]]]


def menu(tipo):
    if tipo == 'login':
        print('-----Menu de login-----')
        print('0-Finalizar')
        print('1-Fazer login como usuário')
        print('2-Fazer login como administrador')
        print('-----------------------')
        op = int(input('Digite a opção desejada: '))
        return op
    elif tipo == 'usuario':
        print('---Menu Principal---')
        print('1-Produtos a venda')
        print('2-Agendar serviços')
        print('0-Sair')
        print('--------------------')
        op = int(input('O que deseja: '))
        return op
    elif tipo == 'adm':
        print('---Menu Principal---')
        print('1-Gerenciar produtos a venda')
        print('2-Gerenciar serviços')
        print('0-Sair')
        print('--------------------')
        op = (input('O que deseja: '))
        return op

def confirmar(login, senha, tipo):
    confirm = []
    confirm.insert(0, [login, senha])
    if confirm[0] in tipo and (len(login.strip()) != 0 and len(senha.strip()) != 0):
        return True
    else:
        return False

def criar(tipo):
    while True:
        login = input('Login: ')
        senha = input('Senha: ')
        cont = 0
        for i in tipo:
            for a in i:
                if a == login:
                    cont += 1
                else:
                    cont += 0
        if cont == 0 and (len(login.strip()) != 0 and len(senha.strip()) != 0):
            tipo.insert(0, [login, senha])
            print(f'Conta criada, seja bem vindo {login}')
            break
        else:
            print('Login existente ou inválido, tente outro')

def listar(tipo):
    if tipo == 'produtos':
        ind = 0
        for i in produtos:
            ind += 1
            print('-------------')
            print(f'{ind}-{i[0]} {i[1]}')
            print(f'Estoque: {i[2]}')
    elif tipo == 'servicos':
        ind = 0
        for i in servicos:
            ind += 1
            print('-------------')
            print(f'{ind}-{i[0]} {i[1]}:')
            hr = 1
            for a in i[2]:
                print(f'{hr}-{a}')
                hr += 1

