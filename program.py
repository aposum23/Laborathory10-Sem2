#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


def add_element(name, num, tm, conn):
    tm = tm.split(' ')
    tm = f'{tm[0]}-{tm[1]}-{tm[2]}'
    cur = conn.cursor()
    query = f"""
    INSERT INTO citys (id, city)
    VALUES
    ({num}, '{name}');
    """
    cur.execute(query)
    conn.commit()

    query = f"""
        INSERT INTO train (train_id, time, city)
        VALUES
        ({num}, '{tm}', {num})
        """
    cur.execute(query)
    conn.commit()
    cur.close()


def find_train(num, conn):
    cur = conn.cursor()
    query = f"""SELECT *
    FROM train
    JOIN citys ON train.city=citys.id
    WHERE train.train_id = {num}"""
    cur.execute(query)
    res = cur.fetchone()
    cur.close()

    if len(res) > 0:
        print(
            f'Конечный пункт: {res[4]} \n'
            f'Номер поезда: {res[0]} \n'
            f'Время отправления: {res[1]}'
        )
        return len(res)
    else:
        print('Поезда с таким номером нет')
        return len(res)


if __name__ == '__main__':
    print('LOADING...')
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS citys(
    id INT PRIMARY KEY,
    city VARCHAR(50));"""

    cur.execute(query)
    conn.commit()

    query = """
        CREATE TABLE IF NOT EXISTS train(
        train_id INT PRIMARY KEY,
        time DATATIME,
        city INT,
        FOREIGN KEY (city) REFERENCES citys(id));"""

    cur.execute(query)
    conn.commit()
    cur.close()
    print('Hello!')

    flag = True
    while flag:
        print('1. Добавить новый поезд')
        print('2. Вывести информацию о поезде')
        print('3.Выход из программы')
        com = int(input('введите номер команды: '))
        if com == 1:
            name = input('city: ')
            num = input('num: ')
            tm = input('tm: ')
            add_element(name, num, tm, conn)
        elif com == 2:
            train_num = input('Введите номер поезда: ')
            length = find_train(train_num, conn)
        elif com == 3:
            flag = False
    conn.close()