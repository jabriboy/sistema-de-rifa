from functions import (
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
        print('[3] Checar bilhetes pegos por pessoa')
        print('[4] Bilhetes entregues')
        print('[5] Bilhetes pagos')
        print('\n[6] Sair')

        opcao = int(input('--->'))

        if opcao == 6:
            break
        elif opcao == 1:
            sys('cls')
            print(verify_ticket())
        elif opcao == 2:
            sys('cls')
            print(verify_person())
        elif opcao == 3:
            sys('cls')
            print(get_all())
        elif opcao == 4:
            sys('cls')
            print(count_tickets())
        elif opcao == 5:
            sys('cls')
            print(count_tickets(pagos=True))