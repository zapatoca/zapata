#!/usr/bin/env python3


def test_mysql(mysql):
    cursor = mysql.cursor()
    cursor.execute('''SHOW DATABASES LIKE 'zapata';''')
    cursor.close()
