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
    while True:
        nome = input('Digite o nome: ')
        tel = input('Digite o telefone: ')
        email = input('Digite email: ')

        id = len(db_pessoa.get_all())

        db_pessoa.insert_one([nome, tel, email, id])

        continuar = int(input('deseja continuar? [0] NÃO [1 SIM]\n-->'))
        if continuar == 0:
            break

def select_ticket(id: int, group=False) -> bool:
    '''
    grava um ticket escolhido com os dados de uma pessoa num banco de dados

    param:
        id: é o número de identificação unico para cada pessoa ja registrada
        group: identifica se é um grupo de bilhetes ou bilhetes individuais
            (obs: se grupo = True todos serão tratados como pago ou não pago)

    return:
        retorna True caso não ocorra erros e False caso alguma condição não for completada
    '''
    if not group:
        while True:
            num = int(input('Digite o numero do ticket: '))
            if db_num.get_by_number(num)[0] == None or db_num.get_by_id(id) == []:
                pagamento = int(input('Pago? [0] NÃO [1] SIM\n--->'))
                if pagamento in [0, 1]:
                    db_num.delete_number(num)
                    pessoa_num = [id, num, pagamento]
                    db_num.insert_one(pessoa_num)
                    print('Bilhete cadastrado com sucesso')
                else:
                    return False
            else:
                print('Número ja escolhido')
                return False
        
            continuar = int(input('deseja continuar? [0] NÃO [1 SIM]\n-->'))
            if continuar == 0:
                return False
    else:
        bilhetes = []
        num_bilhetes = int(input('Digite a quantidade de bilhetes: '))
        for i in range(num_bilhetes):
            bilhete = int(input('Digite o numero do bilhete'))
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
                    return False
        else:
            return False
    
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

def verify_ticket(num: int) -> str:
    '''
    Verifica as informações de um determinado bilhete

    param:
        num: é o numero do bilhete

    return:
        retorna um a tupla com as informações do bilhete (id, num, pago)
            id: id de quem comprou
            num: numero do bilhete
            pago: bool (0 = Não Pago / 1 = Pago)
    '''
    pago = 'Pendente'
    dados = db_num.get_by_number(num)

    if dados[2] == 1:
        pago = 'Aprovado'

    return f'Nome: {db_pessoa.get_by_id(dados[0])[0][0]}\nNúmero: {dados[1]}\nPagamento: {pago}'

def get_all(nome: str, length=False) -> Union[list, bool]:
    '''
    traz uma lista com todos os bilhetes adiquiridos pela pessoa

    param:
        nome: o nome da pessoa q adiquiriu o bilhete
        len: indica se ira calcular o tamanho da lista (True) ou não (false: default)

    return:
        retorna uma lista de tuplas com os dados dos bilhetes, caso não exista essa pessoa retorna False
        se len = True retorna o tamanho da lista de bilhetes, se len = False retorna a própia lista
    '''
    for i in db_pessoa.get_all():
        if i[0] == nome:
            if not length:
                dados = db_num.get_by_id(db_pessoa.get_by_name(nome)[0][3])
                return dados
            else:
                dados = len(db_num.get_by_id(db_pessoa.get_by_name(nome)[0][3]))
                return dados

    return False



if __name__ == '__main__':
    print(__doc__)