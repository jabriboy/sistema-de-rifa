from functions import *

# add pessoa num banco de dados
create_person()


# faz a conexão da pessoa com os bilhetes da rifa
nome = 'nome da pessoa'
pessoa = db_pessoa.get_by_name(nome)[0][3]
select_ticket(pessoa)

