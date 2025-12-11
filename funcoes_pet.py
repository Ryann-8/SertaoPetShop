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

def confirmar(tipo):
    login = input('Login: ')
    senha = input('Senha: ')
    confirm = []
    confirm.insert(0, [login, senha])
    if confirm[0] in tipo and (len(login.strip()) != 0 and len(senha.strip()) != 0):
        print(f'Seja bem vindo, {login}')
    else:
        return False


def criar(tipo):
    print('Login inexistente, crie um: ')
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

def listar(tipo, ti):
    if ti == 'produtos':
        ind = 0
        for i in tipo:
            ind += 1
            print('-------------')
            print(f'{ind}-{i[0]} {i[1]}')
            print(f'Estoque: {i[2]}')
    elif ti == 'servicos':
        ind = 0
        for i in tipo:
            ind += 1
            print('-------------')
            print(f'{ind}-{i[0]} {i[1]}:')
            hr = 1
            for a in i[2]:
                print(f'{hr}-{a}')
                hr += 1

def comprar(qtde, ind, produtos):
    if qtde <= 0:
        print('Valor inválido')
    elif produtos[ind - 1][2] < qtde:
        print('Desculpe, estamos sem estoque desse produto =(')
    else:
        pg = input('Qual será a forma de pagamento? ')
        print('Pagamento confirmado, obrigado pela preferência e volte sempre')
        produtos[ind - 1][2] -= qtde

def agendar(ind, hr, servicos):
    if hr <= len(servicos[ind][2]) and hr > 0:
        pg = input('Qual será a forma de pagamento? ')
        print('Atendimento agendado')
        servicos[ind - 1][2].pop(hr - 1)
    else:
        print('Valor inválido, tente de novo')

def remover(tipo, ti):
    if ti == 'produtos':
        print('1-Remover do estoque')
        print('2-Remover produto por completo')
        remo = int(input('Ação desejada: '))
        if remo == 1:
            ind = int(input('Digite o índice do item que deseja remover estoque: '))
            est = int(input('Quantidade que será a removida do item: '))
            if 0 < est <= tipo[ind - 1][2]:
                tipo[ind - 1][2] -= est
                print('Estoque atualizado')
            else:
                print('Valor invalido (Negativo ou naior que o estoque preexistente)')
        elif remo == 2:
            ind = int(input('Digite o índice do item que deseja remover: '))
            tipo.pop(ind - 1)
            print('Item removido')
    elif ti == 'servicos':
        ind = int(input('Digite o índice do serviço que deseja remover: '))
        tipo.pop(ind - 1)
        print('Serviço removido')

def alterar(tipo, ti):
    if ti == 'produtos':
        ind = int(input('Digite o índice do item que deseja alterar: '))
        a = input('deseja alterar o nome ou o preço?[n/p] ')
        if a == 'n':
            alt = input('Digite o novo nome do item: ')
            tipo[ind - 1][0] = alt
            print('Nome alterado')
        elif a == 'p':
            alt = input('Digite o novo valor do item: ')
            if '-' not in alt:
                tipo[ind - 1][1] = alt
            else:
                print('Valor inválido (Não pode conter - no valor)')
    elif ti == 'servicos':
        ind = int(input('Digite o índice do serviço que deseja alterar: '))
        a = input('deseja alterar o nome o ou preço?[n/p] ')
        if a == 'n':
            alt = input('Digite o novo nome do serviço: ')
            if len(alt.strip()) != 0:
                tipo[ind - 1][0] = alt
                print('Nome alterado')
            else:
                print('nome vazio (ou só com espaços).')
        elif a == 'p':
            alt = input('Digite o novo valor do serviço: ')
            if len(alt.strip()) != 0:
                tipo[ind - 1][1] = alt
                print('Preço alterado')
            else:
                print('nome vazio (ou só com espaços).')

def adicionar(tipo, ti):
    if ti == 'produtos':
        print('1-Adicionar estoque de um item que já está no catálogo')
        print('2-Adicionar novo item')
        ad = int(input('Ação desejada: '))
        if ad == 1:
            ind = int(input('Digite o índice do item que deseja adicionar estoque: '))
            est = int(input('Quantidade que será a dicionada ao item: '))
            if est > 0:
                tipo[ind - 1][2] += est
            else:
                print('Quantidade inválida')
        elif ad == 2:
            ad_n = input('Digite o nome do novo item: ')
            ad_p = input('Digite o preço do novo item: ')
            ad_e = int(input('Quanto será o estoque desse item: '))
            if len(ad_n.strip()) != 0 and len(ad_p.strip()) != 0 and ad_e > 0:
                tipo.append([ad_n, ad_p, ad_e])
                print('Produto adicionado')
            else:
                print('Valores inválidos')
    elif ti == 'servicos':
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
        tipo.append([nome, preco, horarios])
        print('Serviço adicionado')
def alterar_h(tipo):
    ind = int(input('Qual o indice do serviço que você deseja modificar os horarios'))
    op = 99
    while op != '0':
        print('1-Remover horario')
        print('2-Alterar horario')
        print('3-Adicionar horario')
        print('0-Sair')
        op = input('Ação desejada: ')
        if op == '1':
            ind_h = int(input('Qual o indice do horário que será removido: '))
            tipo[ind - 1][2].pop(ind_h - 1)
            print('Horário removido')
        elif op == '2':
            ind_h = int(input('Qual o indice do horário que será alterado: '))
            novo_h = input('Digite o horário que irá substituir o anterior: ')
            tipo[ind - 1][2][ind_h - 1] = novo_h
            print('Horário atualizado')
        elif op == '3':
            novo_h = input('Digite o novo horário: ')
            tipo[ind - 1][2].append(novo_h)
            print('Horario adicionado')