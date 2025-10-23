usuarios = [['ryancliente','cliente123']]
adm = [['ryanadm','adm123']]
produtos = [["Ração para cães"],["Brinquedo de borracha"],["Coleira ajustável"],["Shampoo para pets"],["Caminha confortável"]]
servicos = [["Banho e tosa"],["Consulta veterinária"],["Hospedagem de pets"],["Adestramento"],["Vacinação"]]


print('-----Menu de login-----')
print('1-Fazer login como usuário')
print('2-Fazer login como administrador')
print('-----------------------')
op = int(input('Digite a opção desejada: '))
if op == 1:
    login = input('Login: ')
    senha = input('Senha: ')
    confirm = []
    confirm.insert(0 ,[login,senha])
    if confirm[0][0] == usuarios[0][0] and confirm[0][1] == usuarios[0][1]:
        print(f'Seja bem vindo, {login}')
    else:
        print('Você ainda não possui um login, cadastre-se agora:')
        login = input('Crie um login: ')
        senha = input('crie uma senha: ')
        usuarios.insert(0, [login,senha])
    while op != 0:
        print('---Menu Principal---')
        print('1-Produtos a venda')
        print('2-Agendar serviços')
        print('0-Finalizar')
        print('--------------------')
        op = int(input('O que deseja: '))
        if op == 1:
            ind = 0
            for i in produtos:
                ind += 1
                print('-------------')
                print(f'{ind}-{i[0]}')
            print('-------------')

if op == 2:
    login = input('Login: ')
    senha = input('Senha: ')
    confirm = []
    confirm.insert(0, [login, senha])
    if confirm[0][0] == adm[0][0] and confirm[0][1] == adm[0][1]:
        print(f'Seja bem vindo, {login}')
    else:
        print('Você ainda não possui um login, cadastre-se agora:')
        login = input('Crie um login: ')
        senha = input('crie uma senha: ')
        usuarios.insert(0, [login,senha])

