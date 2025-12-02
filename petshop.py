import funcoes_pet as pet
from funcoes_pet import usuarios
from funcoes_pet import adm
from funcoes_pet import produtos
from funcoes_pet import servicos
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
                pet.listar('produtos')
                ind = int(input('O que deseja comprar? '))
                qtde = int(input('Quantos você deseja comprar?'))
                pet.comprar(qtde, ind)
            elif op == 2:
                pet.listar('servicos')
                ind = int(input('O que deseja marcar? '))
                hr = int(input('Qual horário deseja? '))
                pet.agendar(ind, hr)

    elif op == 2:
        confirm = pet.confirmar(adm)
        if confirm == False:
            pet.criar(adm)
            while op != '0':
                pet.menu('adm')
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
                                if 0 < est <= produtos[ind-1][2]:
                                    produtos[ind-1][2] -= est
                                    print('Estoque atualizado')
                                else:
                                    print('Valor invalido (Negativo ou naior que o estoque preexistente)')
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
                                if '-' not in alt:
                                    produtos[ind-1][1] = alt
                                else:
                                    print('Valor inválido (Não pode conter - no valor)')
                        elif op == 3:
                            print('1-Adicionar estoque de um item que já está no catálogo')
                            print('2-Adicionar novo item')
                            ad = int(input('Ação desejada: '))
                            if ad == 1:
                                ind = int(input('Digite o índice do item que deseja adicionar estoque: '))
                                est = int(input('Quantidade que será a dicionada ao item: '))
                                if est > 0:
                                    produtos[ind-1][2] += est
                                else:
                                    print('Quantidade inválida')
                            elif ad == 2:
                                ad_n = input('Digite o nome do novo item: ')
                                ad_p = input('Digite o preço do novo item: ')
                                ad_e = int(input('Quanto será o estoque desse item: '))
                                if len(ad_n.strip()) != 0 and len(ad_p.strip()) != 0 and ad_e >0:
                                    produtos.append([ad_n,ad_p,ad_e])
                                    print('Produto adicionado')
                                else:
                                    print('Valores inválidos')
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