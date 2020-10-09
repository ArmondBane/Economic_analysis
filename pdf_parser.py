import csv
import os
import sqlite3
from datetime import datetime
import re

import camelot


def parse_pdf_to_database(pdf_path, pdf_id, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    table = camelot.read_pdf(pdf_path, pages='1,2,3,4')
    table.export('export.csv', f='csv', compress=False)

    if not is_execute_right():
        return -1

    cursor.execute("INSERT INTO economic_files VALUES ('" + pdf_id + "','file1.pdf')")
    conn.commit()

    read_and_insert_files(cursor, conn)
    delete_files()

def read_and_insert_files(cursor, conn):
    insert_data_to_table(cursor, conn, 'export-page-1-table-2.csv', "Таблица_Актив", 3)
    insert_data_to_table(cursor, conn, 'export-page-2-table-1.csv', "Таблица_Пассив", 3)
    insert_data_to_table(cursor, conn, 'export-page-3-table-2.csv', "Таблица_Чистая_прибыль", 2)
    insert_data_to_table(cursor, conn, 'export-page-4-table-1.csv', "Таблица_Разводненная_прибыль", 2)

# функция построчной вставки характерстик из таблицы в ДБ
def insert_data_to_table(cursor, conn, file, table, years_amount):
    with open(file, encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        i = 0
        while i < years_amount:
            colomn = 2+years_amount
            str = insert_in_table_str(table, '1', (2020 - years_amount + i).__str__())
            for row in data:
                if re.match(r'^[0-9]{4}$', row[2]):
                    row[colomn - i] = row[colomn - i].replace("(", "")
                    row[colomn - i] = row[colomn - i].replace(")", "")
                    row[colomn - i] = row[colomn - i].replace(" ", "")
                    if re.match(r'^[0-9]*$', row[colomn - i]):
                        str += ",'" + row[colomn - i] + "'"
                    else:
                        str += ", '0'"
            str += ")"
            cursor.execute(str)
            conn.commit()
            i += 1

def insert_in_table_str(name, id, date):
    now = datetime.now()
    return "INSERT INTO " + name + " VALUES ('" + now.microsecond.__str__() + "', '" + id + "', '" + date + "'"

def delete_files():
    os.remove('export-page-1-table-2.csv')
    os.remove('export-page-2-table-1.csv')
    os.remove('export-page-3-table-2.csv')
    os.remove('export-page-4-table-1.csv')
    os.remove('export-page-1-table-1.csv')
    os.remove('export-page-3-table-1.csv')

def is_execute_right():
    right = True
    if not os.path.isfile('export-page-1-table-2.csv'):
        right = False
    if not os.path.isfile('export-page-2-table-1.csv'):
        right = False
    if not os.path.isfile('export-page-3-table-2.csv'):
        right = False
    if not os.path.isfile('export-page-4-table-1.csv'):
        right = False
    if not os.path.isfile('export-page-1-table-1.csv'):
        right = False
    if not os.path.isfile('export-page-3-table-1.csv'):
        right = False
    return right