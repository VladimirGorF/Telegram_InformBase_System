import sqlite3
import datetime


conn = sqlite3.connect('taxi_drivers.db')
cur = conn.cursor()

def sql_update(list_param):    # принимает  входящий спискок изменений
    all_columns = ["userid", "full_name", "identification_number", "rating", "auto", "fines", "telefon", "last_modified"]
    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M")

    for i in range(1, len(list_param)):
        if not list_param[i]:
            print('Not value')
        else:                      # изменяет данные в соответствуещем поле
            cur.execute(f' UPDATE drivers SET {all_columns[i]} = "{list_param[i]}" where userid = {list_param[0]}')
            conn.commit()

    cur.execute(f' UPDATE drivers SET {all_columns[-1]} = "{time}" where userid = {list_param[0]}')  #вносит дату и время
    conn.commit()
    return cur.execute(f'SELECT * FROM drivers where userid = {list_param[0]} ')     # возвращает обновленные данные


