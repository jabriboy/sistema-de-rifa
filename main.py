from functions import *
from show_data import menu
from os import system as sys

while True:
    sys('cls')

    print('O QUE DESEJA FAZER?')
    print('[1] Criar um novo cadastro')
    print('[2] Adicionar bilhetes para pessoas cadastradas')
    print('[3] Atualizar dados de bilhetes')
    print('[4] Atualizar dados de uma pessoa')
    print('[5] Buscar informações')
    print('\n[6] Sair')

    opcao = int(input('--->'))

    if opcao == 6:
        sys('cls')
        exit()
    elif opcao == 1:
        sys('cls')
        create_person()
    elif opcao == 2:
        sys('cls')
        select_ticket()
    elif opcao == 3:
        sys('cls')
        update_ticket()
    elif opcao == 4:
        sys('cls')
        update_pessoa()
    elif opcao == 5:
        sys('cls')
        menu()
