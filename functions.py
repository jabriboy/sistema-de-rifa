'''
Módulo de funções para criar e selecionar bilhetes de rifa
autor: jabriboy
'''
from typing import Union
import data_base as db_num
import data_base_pessoa as db_pessoa

def create_person() -> None:
    '''
    Cria e grava os dados de uma pessoa num banco de dados
    '''
    nome = input('Digite o nome: ')
    tel = input('Digite o telefone: ')

    id = len(db_pessoa.get_all())
    db_pessoa.insert_one([nome, tel, '', id])

def select_ticket() -> bool:
    '''
    grava um ticket escolhido com os dados de uma pessoa num banco de dados

    param:
        group: identifica se é um grupo de bilhetes ou bilhetes individuais
            (obs: se grupo = True todos serão tratados como pago ou não pago)

    return:
        retorna True caso não ocorra erros e False caso alguma condição não for completada
    '''
    nome = input('Digite o nome da pessoa: ')
    
    if db_pessoa.get_by_name(nome):
        id = db_pessoa.get_by_name(nome)[0][3]
        bilhetes = []
        num_bilhetes = int(input('Digite a quantidade de bilhetes: '))
        for i in range(num_bilhetes):
            bilhete = int(input('Digite o numero do bilhete: '))
            bilhetes.append(bilhete)

        pagamento = int(input('Pago? [0] NÃO [1] SIM\n--->'))
        if pagamento in [0, 1]:
            for i in bilhetes:
                if db_num.get_by_number(i)[0] == None or db_num.get_by_id(id) == []:
                    db_num.delete_number(i)
                    pessoa_num = [id, i, pagamento]
                    db_num.insert_one(pessoa_num)
                    print('Bilhete cadastrado com sucesso')
                else:
                    print('Número ja escolhido')
                    continuar = input('Aperte qualquer tecla para continuar--->')
                    return False
        else:
            return False
    else:
        continuar = int(input("Pessoa não cadastrada, deseja cadastrar? [1] sim | [0] não: "))
        if(continuar == 1):
            create_person()
            select_ticket()
        else:
            return False
    
    continuar = input('Aperte qualquer tecla para continuar--->')
    return True

def count_tickets(pagos=False) -> int:
    '''
    conta quantos bilhetes foram adiquiridos no total

    param:
        pagos: caso True retorna somente os tickets ja pagos, se falso retorna todos bilhetes adiquiridos

    return:
        retorna a quantidade de bilhetes (int) adiquiridos/reservados
    '''
    count = 0
    if not pagos:
        for i in db_num.get_all():
            if i[0] != None:
                count += 1
    else:
        for i in db_num.get_all():
            if i[2] == 1:
                count += 1

    return count

def verify_ticket() -> str:
    '''
    Verifica as informações de um determinado bilhete

    return:
        retorna um a tupla com as informações do bilhete (id, num, pago)
            id: id de quem comprou
            num: numero do bilhete
            pago: bool (0 = Não Pago / 1 = Pago)
    '''
    num = int(input('Digite o numero do bilhete: '))
    pago = 'Pendente'

    if db_num.get_by_number(num)[0] != None:
        dados = db_num.get_by_number(num)
        
        if dados[2] == 1:
            pago = 'Aprovado'

        return f'Nome: {db_pessoa.get_by_id(dados[0])[0]}\nNúmero: {dados[1]}\nPagamento: {pago}'
    
    return f'Nome: {None}\nNúmero: {num}\nPagamento: {pago}'

def verify_person() -> Union[tuple, str]:
    '''
    verifica se a pessoa esta cadastrada no banco de dados

    return:
        se existir pessoa cadastrada com o mesmo nome, é retornada um iterável com os cadastro de mesmo nome
        se não existir é retornado uma str com aviso de pessoa não cadastrada
    '''
    i = 0
    nome = input('Digite o nome da pessoa: ')

    for pessoa in db_pessoa.get_by_name(nome):
        if nome in pessoa[i]:
            return db_pessoa.get_by_name(nome)
        i += 1
    else:
        return 'Pessoa não cadastrada'

def get_all() -> Union[list, bool]:
    '''
    traz uma lista com todos os bilhetes adiquiridos pela pessoa

    return:
        retorna uma lista de tuplas com os dados dos bilhetes, caso não exista essa pessoa retorna False
        se len = True retorna o tamanho da lista de bilhetes, se len = False retorna a própia lista
    '''
    nome = input('Digite o nome: ')
    print('Deseja saber a quantidade de bilhetes ou o numero dos bilhetes?')
    print('[1] Quantidade\n[2] Numero dos bilhetes')
    
    escolha = int(input('--->'))

    if escolha == 1:
        length = True
    else:
        length = False

    for i in db_pessoa.get_all():
        if i[0] == nome:
            if not length:
                dados = db_num.get_by_id(db_pessoa.get_by_name(nome)[0][3])
                return dados
            else:
                dados = len(db_num.get_by_id(db_pessoa.get_by_name(nome)[0][3]))
                return dados

    return False

def check_pessoa():
    '''
    busca no banco de dados pessoas cadastradas pelo prefixo

    return:
        retorna uma lista com todos os nomes com a inicial desejada
    '''
    total = []
    for x in db_pessoa.get_all():
        total.append(x[0])

    nome = input('Digite o nome: ')

    prefixo = [ s for s in total if s.startswith(nome) ]

    return prefixo

def update_ticket() -> bool:
    '''
    atualiza os dados de um bilhete, caso houver devolução ou pagamento de um bilhete não pago

    param:
        num: o numero do bilhete

    return:
        retorna True quando a atualização é bem sucedida e False quando ocorre algum erro
    '''
    bilhetes = []
    
    qnt_bilhetes = int(input('Digite a quantidade de bilhetes: '))
    for _ in range(qnt_bilhetes):
        num_bilhetes = int(input('Digite o numero do bilhete: '))
        bilhetes.append(num_bilhetes)

    print('O que deseja alterar?')
    print('[0] ID\n[1] PAGAMENTO\n[2] ID e PAGAMENTO')
    opcao = int(input('--->'))

    if opcao in [0, 1, 2]:
        if opcao == 0:
            nome = input('Digite o nome do novo dono: ')
            if db_pessoa.get_by_name(nome):
                novo_id = db_pessoa.get_by_name(nome)[0][3]
                for n in bilhetes:
                    _, _, situacao = db_num.get_by_number(n)
                    db_num.delete_number(n)
                    novo_bilhete = novo_id, n, situacao
                    db_num.insert_one(novo_bilhete)

                return True
            else:
                continuar = int(input("Pessoa não cadastrada, deseja cadastrar? [1] sim | [0] não: "))
                if(continuar == 1):
                    create_person()
                    nome = input('Digite o nome do novo dono: ')
                    if db_pessoa.get_by_name(nome):
                        novo_id = db_pessoa.get_by_name(nome)[0][3]
                        for n in bilhetes:
                            _, _, situacao = db_num.get_by_number(n)
                            db_num.delete_number(n)
                            novo_bilhete = novo_id, n, situacao
                            db_num.insert_one(novo_bilhete)

                        return True
                    else:
                        return False
                else:
                    return False

        elif opcao == 1:
            nova_situacao = int(input('Digite a nova situação do pagamento: '))
            if nova_situacao in [0, 1]:
                for n in bilhetes:
                    id, _, _ = db_num.get_by_number(n)
                    db_num.delete_number(n)
                    novo_bilhete = id, n, nova_situacao
                    db_num.insert_one(novo_bilhete)

                return True
            return False

        else:
            nome = input('Digite o nome do novo dono: ')
            nova_situacao = int(input('Digite a nova situação do pagamento: '))
            if db_pessoa.get_by_name(nome) and nova_situacao in [0, 1]:
                for n in bilhetes:
                    novo_id = db_pessoa.get_by_name(nome)[0][3]
                    db_num.delete_number(n)
                    novo_bilhete = novo_id, n, nova_situacao
                    db_num.insert_one(novo_bilhete)

                return True
            elif db_pessoa.get_by_name(nome) == None:
                continuar = int(input("Pessoa não cadastrada, deseja cadastrar? [1] sim | [0] não: "))
                if(continuar == 1):
                    create_person()
                    nome = input('Digite o nome do novo dono: ')
                    if db_pessoa.get_by_name(nome) and nova_situacao in [0, 1]:
                        for n in bilhetes:
                            novo_id = db_pessoa.get_by_name(nome)[0][3]
                            db_num.delete_number(n)
                            novo_bilhete = novo_id, n, nova_situacao
                            db_num.insert_one(novo_bilhete)

                        return True
                    else:
                        return False
                else:
                    return False
            else:
                nova_situacao = int(input('Digite a nova situação do pagamento: '))
                if nova_situacao in [0, 1]:
                    if db_pessoa.get_by_name(nome) and nova_situacao in [0, 1]:
                        for n in bilhetes:
                            novo_id = db_pessoa.get_by_name(nome)[0][3]
                            db_num.delete_number(n)
                            novo_bilhete = novo_id, n, nova_situacao
                            db_num.insert_one(novo_bilhete)

                        return True
                    else:
                        return False
                else:
                    return False
            return False

    return False

def update_pessoa() -> Union[tuple, bool]:
    '''
    Atualiza uma ou mais informações de uma pessoa
    '''
    nome = input('Digite o nome da pessoa: ')
    _, tel, email, id = db_pessoa.get_by_name(nome)[0]
    print('O que deseja mudar?')
    print('[0] NOME\n[1] telefone\n[2] email\n[3] TUDO')
    opcao = int(input('--->'))

    if opcao == 0:
        novo_nome = input('Digite o novo nome: ')
        nova_pessoa = novo_nome, tel, email, id
        db_pessoa.delete_by_id(id)
        db_pessoa.insert_one(nova_pessoa)

        return nova_pessoa

    elif opcao == 1:
        novo_tel = input('Digite o novo telefone: ')
        nova_pessoa = nome, novo_tel, email, id
        db_pessoa.delete_by_id(id)
        db_pessoa.insert_one(nova_pessoa)

        return nova_pessoa

    elif opcao == 2:
        novo_email = input('Digite o novo email: ')
        nova_pessoa = nome, tel, novo_email, id
        db_pessoa.delete_by_id(id)
        db_pessoa.insert_one(novo_email)

        return nova_pessoa

    elif opcao == 3:
        novo_nome = input('Digite o novo nome: ')
        novo_tel = input('Digite o novo telefone: ')
        novo_email = input('Digite o novo email: ')
        nova_pessoa = novo_nome, novo_tel, novo_email, id
        db_pessoa.delete_by_id(id)
        db_pessoa.insert_one(nova_pessoa)

        return nova_pessoa

    return False


if __name__ == '__main__':
    print(__doc__)
