import funcoes_pet as pet
usuarios = {'ryancliente': 'cliente123'}
adms = {'ryanadm': 'adm123'}
produtos = [["Ração para cães", "R$60", 5],
            ["Brinquedo de borracha", "R$60", 5],
            ["Coleira ajustável", "R$60", 5],
            ["Shampoo para pets", "R$60", 5],
            ["Caminha confortável", "R$60", 5]]
servicos = [["Banho e tosa", "R$100", ["Às 10H", "Às 14H"]],
            ["Consulta veterinária", "R$100", ["Às 10H", "Às 14H"]],
            ["Hospedagem de pets", "R$100", ["Às 10H", "Às 14H"]],
            ["Adestramento", "R$100", ["Às 10H", "Às 14H"]],
            ["Vacinação", "R$100", ["Às 10H", "Às 14H"]]]
while True:
    op = pet.menu('login')
    if op == 0:
        break
    elif op == 1:
        login = input('Login: ')
        senha = input('Senha: ')
        confirm = pet.confirmar(login, senha, usuarios)
        if confirm:
            print('Seja bem vindo(a)')
            pet.capturar(login)
        else:
            criando = pet.criar(usuarios)
            pet.capturar(criando)
        while op != 0:
            op = pet.menu('usuario')
            if op == 1:
                pet.listar(produtos, 'produtos')
                ind = int(input('O que deseja comprar? '))
                qtde = int(input('Quantos você deseja comprar?'))
                pet.comprar(qtde, ind, produtos)
            elif op == 2:
                pet.listar(servicos, 'servicos')
                ind = int(input('O que deseja marcar? '))
                hr = int(input('Qual horário deseja? '))
                pet.agendar(ind, hr, servicos)

    elif op == 2:
        login = input('Login: ')
        senha = input('Senha: ')
        confirm = pet.confirmar(login, senha, adms)
        if confirm:
            print('Seja bem vindo(a)')
            pet.capturar(login)
        else:
            criando = pet.criar(adms)
            pet.capturar(criando)
        while op != '0':
            op = pet.menu('adm')
            if op == '1':
                print('---Produtos a venda---')
                pet.listar(produtos, 'produtos')
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
                        pet.remover(produtos, 'produtos')
                    elif op == 2:
                        pet.alterar(produtos, 'produtos')
                    elif op == 3:
                        pet.adicionar(produtos, 'produtos')
                    elif op == 4:
                        pet.listar(produtos, 'produtos')
            elif op == '2':
                print('---Serviços disponíveis---')
                pet.listar(servicos, 'servicos')
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
                        pet.remover(servicos, 'servicos')
                    elif op == 2:
                        pet.alterar(servicos, 'servicos')
                    elif op == 3:
                        pet.adicionar(servicos, 'servicos')
                    elif op == 4:
                        pet.listar(servicos, 'servicos')
                    elif op == 5:
                        pet.alterar_h(servicos)
                    else:
                        print('Valor inválido, tente uma das opções')
