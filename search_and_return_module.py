import sqlite3
conn = sqlite3.connect('taxi_drivers.db')
cur = conn.cursor()


# Вывод данных по параметрам
def search_param(list_param):
    # Создаем два списка . В списке list_keys находятся столбцы параметров поиска , в list_values находятся значения параметров поиска
    list_keys=[]
    list_values=[]
    all_columns = ["userid", "full_name", "identification_number", "rating", "auto", "fines", "telefon", "last_modified"]
    for i,j in enumerate(list_param):
        if j!='':
            list_keys.append(all_columns[i])
            list_values.append(j)
    sql_request = ''
    # Определяем сколько параметров передал пользователь и формируем запрос
    if len(list_keys) > 1:
        len_list=len(list_keys)
        count=0
        while len_list:
            sql_request+='{}="{}" AND '.format(list_keys[count],list_values[count])
            len_list-=1
            count+=1
        sql_request=sql_request[:-4]
        cur.execute(f"""SELECT * FROM drivers WHERE {sql_request}""")
    else:
        sql_request += '{}="{}"'.format(list_keys[0], list_values[0])
        cur.execute(f"""SELECT * FROM drivers WHERE {sql_request}""")
    result_list=cur.fetchall()
    return_list=[list(i) for i in result_list]
    return return_list


# Вывод всех данных из таблицы
def search_all():
    cur.execute("SELECT * FROM drivers")
    result_list = cur.fetchall()
    return_list = [list(i) for i in result_list]
    return return_list

# abc=search_all()
# result_list=[]
# for i in abc:
#     result_list.append(list(i))
#
# print(result_list)