usuarios = [['ryancliente','cliente123']]
adm = [['ryanadm','adm123']]
produtos = [["Ração para cães", "R$60", 5],["Brinquedo de borracha", "R$60", 5],["Coleira ajustável", "R$60", 5],["Shampoo para pets", "R$60", 5],["Caminha confortável", "R$60", 5]]
servicos = [["Banho e tosa", "R$100", ["Às 10H", "Às 14H"]],["Consulta veterinária", "R$100", ["Às 10H", "Às 14H"]],["Hospedagem de pets", "R$100", ["Às 10H", "Às 14H"]],["Adestramento", "R$100", ["Às 10H", "Às 14H"]],["Vacinação", "R$100", ["Às 10H", "Às 14H"]]]
while True:
    print('-----Menu de login-----')
    print('0-Finalizar')
    print('1-Fazer login como usuário')
    print('2-Fazer login como administrador')
    print('-----------------------')
    op = int(input('Digite a opção desejada: '))
    if op == 0:
        break
    elif op == 1:
        login = input('Login: ')
        senha = input('Senha: ')
        confirm = []
        confirm.insert(0 ,[login,senha])
        if confirm[0] in usuarios:
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
            print('0-Sair')
            print('--------------------')
            op = int(input('O que deseja: '))
            if op == 1:
                ind = 0
                for i in produtos:
                    ind += 1
                    print('-------------')
                    print(f'{ind}-{i[0]} {i[1]}')
                    print(f'Estoque: {i[2]}')
                ind = int(input('O que deseja comprar? '))
                pg = input('Qual será a forma de pagamento? ')
                if produtos[ind-1][2] == 0:
                    print('Desculpe, estamos sem estoque desse produto =(')
                else:
                    print('Pagamento confirmado, obrigado pela preferência e volte sempre')
                    produtos[ind-1][2] -= 1
            elif op == 2:
                ind = 0
                for i in servicos:
                    ind += 1
                    print('-------------')
                    print(f'{ind}-{i[0]} {i[1]}:')
                    hr = 1
                    for a in i[2]:
                        print(f'{hr}-{a}')
                        hr += 1
                ind = int(input('O que deseja marcar? '))
                hr = int(input('Qual horário deseja? '))

                pg = input('Qual será a forma de pagamento? ')
                print('Pagamento confirmado, obrigado pela preferência e volte sempre')
                servicos[ind-1][2].pop(hr-1)
    if op == 2:
        login = input('Login: ')
        senha = input('Senha: ')
        confirm = []
        confirm.insert(0, [login, senha])
        if confirm[0] in adm:
            print(f'Seja bem vindo, {login}')
        else:
            print('Você ainda não possui um login, cadastre-se agora:')
            login = input('Crie um login: ')
            senha = input('crie uma senha: ')
            usuarios.insert(0, [login,senha])
        while op != '0':
            print('---Menu Principal---')
            print('1-Gerenciar produtos a venda')
            print('2-Gerenciar serviços')
            print('0-Sair')
            print('--------------------')
            op = (input('O que deseja: '))
            if op == '1':
                print('---Produtos a venda---')
                ind = 1
                for i in produtos:
                    print(f'{ind}-{i[0]} {i[1]}')
                    ind += 1
                while op != 0:
                    print('---------------')
                    print('0-sair')
                    print('1-Remover item')
                    print('2-Alterar item')
                    print('3-Adiconar item')
                    print('4-listar itens')
                    op = int(input('Ação desejada: '))
                    ind = 1
                    if op == 1:
                        print('1-Remover do estoque')
                        print('2-Remover produto por completo')
                        remo = int(input('Ação desejada: '))
                        if remo == 1:
                            ind = int(input('Digite o índice do item que deseja remover estoque: '))
                            est = int(input('Quantidade que será a removida do item: '))
                            produtos[ind-1][2] -= est
                        elif remo == 2:
                            ind = int(input('Digite o índice do item que deseja remover: '))
                            produtos.pop(ind-1)
                            print('Item removido')
                    elif op == 2:
                        ind = int(input('Digite o índice do item que deseja alterar: '))
                        a = input('deseja alterar o nome ou o preço?[n/p] ')
                        if a == 'n':
                            alt = input('Digite o novo nome do item: ')
                            produtos[ind-1][0] = alt
                            print('Nome alterado')
                        elif a == 'p':
                            alt = input('Digite o novo valor do item: ')
                            produtos[ind-1][1] = alt
                    elif op == 3:
                        print('1-Adicionar estoque de um item que já está no catálogo')
                        print('2-Adicionar novo item')
                        ad = int(input('Ação desejada: '))
                        if ad == 1:
                            ind = int(input('Digite o índice do item que deseja adicionar estoque: '))
                            est = int(input('Quantidade que será a dicionada ao item: '))
                            produtos[ind-1][2] += est
                        elif ad == 2:
                            ad_n = input('Digite o nome do novo item: ')
                            ad_p = input('Digite o preço do novo item: ')
                            ad_e = int(input('Quanto será o estoque desse item: '))
                            produtos.append([ad_n,ad_p,ad_e])
                            print('Produto adicionado')
                    elif op == 4:
                        for i in produtos:
                            print('----------')
                            print(f'{ind}-{i[0]} {i[1]}')
                            print(f'Estoque: {i[2]}')
                            ind += 1
            elif op == '2':
                print('---Serviços disponíveis---')
                ind = 0
                for i in servicos:
                    ind += 1
                    print('-------------')
                    print(f'{ind}-{i[0]} {i[1]}:')
                    hr = 1
                    for a in i[2]:
                        print(f'{hr}-{a}')
                        hr += 1
                while op != 0:
                    print('---------------')
                    print('0-sair')
                    print('1-Remover serviço')
                    print('2-Alterar serviço')
                    print('3-Adiconar serviço')
                    print('4-listar serviços')
                    print('5-Remover/Alterar/Adicionar horários')
                    op = int(input('Ação desejada: '))
                    if op == 1:
                        ind = int(input('Digite o índice do serviço que deseja remover: '))
                        servicos.pop(ind - 1)
                        print('Serviço removido')
                    elif op == 2:
                        ind = int(input('Digite o índice do serviço que deseja alterar: '))
                        a = input('deseja alterar o nome o ou preço?[n/p/h] ')
                        if a == 'n':
                            alt = input('Digite o novo nome do serviço: ')
                            servicos[ind - 1][0] = alt
                            print('Nome alterado')
                        elif a == 'p':
                            alt = input('Digite o novo valor do serviço: ')
                            servicos[ind - 1][1] = alt
                    elif op == 3:
                        nome = input('Digite o novo serviço: ')
                        preco = input('quanto irá custar: ')
                        horas = 99
                        horarios = []
                        while horas != 0:
                            print('1-Adicionar horários disponíveis para o serviço')
                            print('0-sair')
                            horas = int(input('Ação desejada: '))
                            if horas == 1:
                                hora = input('Digite o horário: ')
                                horarios.append(hora)
                        servicos.append([nome,preco,horarios])
                        print('Serviço adicionado')
                    elif op == 4:
                        ind = 0
                        for i in servicos:
                            ind += 1
                            print('-------------')
                            print(f'{ind}-{i[0]} {i[1]}:')
                            hr = 1
                            for a in i[2]:
                                print(f'{hr}-{a}')
                                hr += 1
                    elif op == 5:
                        ind = int(input('Qual o indice do serviço que você deseja modificar os horarios'))
                        while op != '0':
                            print('1-Remover horario')
                            print('2-Alterar horario')
                            print('3-Adicionar horario')
                            print('0-Sair')
                            op = input('Ação desejada: ')
                            if op == '1':
                                ind_h = int(input('Qual o indice do horário que será removido: '))
                                servicos[ind-1][2].pop(ind_h-1)
                                print('Horário removido')
                            elif op == '2':
                                ind_h = int(input('Qual o indice do horário que será alterado: '))
                                novo_h = input('Digite o horário que irá substituir o anterior: ')
                                servicos[ind-1][2][ind_h-1] = novo_h
                                print('Horário atualizado')
                            elif op == '3':
                                novo_h = input('Digite o novo horário: ')
                                servicos[ind-1][2].append(novo_h)
                                print('Horario adicionado')