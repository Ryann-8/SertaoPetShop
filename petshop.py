usuarios = [['ryancliente','clinte123']]
adm = [['denisadm','adm123']]
op = 99
s_n = input('Olá, seja bem vindo, você ja possui cadastro?[s/n] ')
if s_n == 'n':
    while op != 0:
        print('------Cadastro------')
        print('0-Sair para o Menu')
        print('1-Cadastrar administrador')
        print('2-Cadastrar usuário')
        print('--------------------')
        op = int(input('digite a opção desejada'))
        if op == 1:
            login= input('digite um login: ')
            senha = input('digite uma senha: ')
            adm.append([login,senha])
            print('Cadastro concluído')
        elif op == 2:
            login = input('digite um login: ')
            senha = input('digite uma senha: ')
            usuarios.append([login,senha])
            print('Cadastro concluído')
#elif s_n == 's':