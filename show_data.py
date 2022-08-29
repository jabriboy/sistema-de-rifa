from functions import (
    check_pessoa,
    count_tickets,
    verify_ticket,
    verify_person,
    get_all
    )

from os import system as sys

def menu():
    while True:
        print('O QUE DESEJA SABER?')
        print('[1] Situação do bilhete')
        print('[2] Checar cadastro de pessoa')
        print('[3] Checar nomes pela letra')
        print('[4] Checar bilhetes pegos por pessoa')
        print('[5] Bilhetes entregues')
        print('[6] Bilhetes pagos')
        print('\n[7] Sair')

        opcao = int(input('--->'))

        if opcao == 7:
            break
        elif opcao == 1:
            sys('cls')
            print(verify_ticket())
        elif opcao == 2:
            sys('cls')
            print(verify_person())
        elif opcao == 3:
            sys('cls')
            print(check_pessoa())
        elif opcao == 4:
            sys('cls')
            print(get_all())
        elif opcao == 5:
            sys('cls')
            print(count_tickets())
        elif opcao == 6:
            sys('cls')
            print(count_tickets(pagos=True))