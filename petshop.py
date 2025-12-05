import funcoes_pet as pet
usuarios = [['ryancliente','cliente123']]
adm = [['ryanadm','adm123']]
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
        confirm = pet.confirmar(usuarios)
        if confirm == False:
            pet.criar(usuarios)
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
        confirm = pet.confirmar(adm)
        if confirm == False:
            pet.criar(adm)
            while op != '0':
                pet.menu('adm')
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
                            pet.remover(produtos)
                        elif op == 2:
                            pet.alterar(produtos)
                        elif op == 3:
                            pet.adicionar(produtos)
                        elif op == 4:
                            pet.listar(produtos, 'produtos')
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
                            a = input('deseja alterar o nome o ou preço?[n/p] ')
                            if a == 'n':
                                alt = input('Digite o novo nome do serviço: ')
                                if len(alt.strip()) != 0:
                                    servicos[ind - 1][0] = alt
                                    print('Nome alterado')
                                else:
                                    print('nome vazio (ou só com espaços).')
                            elif a == 'p':
                                alt = input('Digite o novo valor do serviço: ')
                                if len(alt.strip()) != 0:
                                    servicos[ind - 1][1] = alt
                                    print('Preço alterado')
                                else:
                                    print('nome vazio (ou só com espaços).')
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
                        else:
                            print('Valor inválido, tente uma das opções')
        else:
            print('Login ou senha vazios (ou só com espaços).')