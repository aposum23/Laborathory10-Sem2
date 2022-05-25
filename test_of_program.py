#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import program
import sqlite3
import datetime


def add_train(conn):
    program.add_element('Moscow', '25', '2022 6 3', conn)
    cur = conn.cursor()
    query = """SELECT *
                FROM train
                WHERE train_id = 25"""
    cur.execute(query)
    res = cur.fetchall()
    return len(res) > 0

def find_train(conn):
    length = program.find_train('25', conn)
    return length > 0

if __name__ == '__main__':
    conn = sqlite3.connect('data.db')
    res = add_train(conn)
    print(f'add train: {res}')
    res = find_train(conn)
    print(f'find train: {res}')
