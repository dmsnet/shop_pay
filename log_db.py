__author__ = 'dmsnet'

# -- coding: utf-8 --


import psycopg2
import psycopg2.extras
import sys, constants


def add_pay(data):
    conn = psycopg2.connect(constants.conn_string)
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    cur.execute("INSERT INTO tb_pay_log ( sum, ccy, descr, status, created_at, updated_at) VALUES (%s, %s, %s, %s , now(), null) "+
                "RETURNING tb_pay_log.id ;", [data['summ'], data['sel'], data['txt'], 'payopen' ])
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows[0][0]

def get_last():
    conn = psycopg2.connect(constants.conn_string)
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    cur.execute("select id, sum, ccy, descr, status, created_at, updated_at from tb_pay_log order by created_at desc limit 100")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows




