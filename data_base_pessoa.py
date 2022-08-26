'''
Módulos de funções para criação e manipulação de BD de pessoas
autor: jabriboy
'''

import sqlite3

conn = sqlite3.connect('pessoa_data_base.db')

c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE pessoa_database (
        name text,
        tel text,
        email text,
        id int
        )""")

def drop_table():
    c.execute("DROP TABLE pessoa_database")
    conn.commit()

def insert_one(person: list) -> bool:
    with conn:
        c.execute("INSERT INTO pessoa_database VALUES (:name, :telefone, :email, :id)", person)

def get_by_name(name: str):
    c.execute("SELECT * FROM pessoa_database WHERE name = :name", {'name': name})
    return c.fetchall()

def get_by_id(id: int):
    c.execute("SELECT * FROM pessoa_database WHERE id = :id", {'id': id})
    return c.fetchone()

def get_by_number(rifa_num: int):
    c.execute("SELECT * FROM pessoa_database WHERE numbers = :numbers", {'numbers': rifa_num})
    return c.fetchone()

def delete_by_name(person_name):
    with conn:
        c.execute("DELETE from pessoa_database WHERE name = :name", {'name': person_name})

def delete_by_id(person_id):
    with conn:
        c.execute("DELETE from pessoa_database WHERE id = :id", {'id': person_id})

def get_all():
    with conn:
        c.execute("SELECT * FROM pessoa_database")
        return c.fetchall()


if __name__ == '__main__':
    print(__doc__)
