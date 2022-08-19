'''
Módulos de funções para criação e manipulação de BD dos bilhetes da rifa
autor: jabriboy
'''

import sqlite3

conn = sqlite3.connect('rifa_data_base.db')

c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE database (
        id int,
        numbers int,
        pago int
        )""")

def drop_table():
    c.execute("DROP TABLE database")
    conn.commit()

def reset_table():
    for num in range(0, 10000):
        vazio = [None, num, 0]
        with conn:
            c.execute("INSERT INTO database VALUES (:id, :tickets, :pago)", vazio)

def insert_one(person):
    with conn:
        c.execute("INSERT INTO database VALUES (:id, :tickets, :pago)", person)

def delete_number(num: int):
    with conn:
        c.execute("DELETE from database WHERE numbers = :numbers", {'numbers': num})

def get_by_id(id: int):
    c.execute("SELECT * FROM database WHERE id = :id", {'id': id})
    return c.fetchall()

def get_by_number(rifa_num: int):
    c.execute("SELECT * FROM database WHERE numbers = :numbers", {'numbers': rifa_num})
    return c.fetchone()

def get_all():
    with conn:
        c.execute("SELECT * FROM database")
        return c.fetchall()

if __name__ == '__main__':
    print(__doc__)
