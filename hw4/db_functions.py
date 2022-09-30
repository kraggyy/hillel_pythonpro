import sqlite3
import os

from typing import List


def execute_query(query_sql: str) -> List:
    """
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    """
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cursor = connection.cursor()
    result = cursor.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    """
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    """
    for record in records:
        print(*record)


def get_filtered_customers(city=None,
                           state=None) -> List:
    """
    Возвращает клиентов, отфильтрованных по городу и штату
    :param city: город проживания, строка
    :param state: штат проживания, строка
    :return: список клиентов
    """
    query_sql = '''
        SELECT *
          FROM customers
    '''
    if city and state:
        query_sql += f" WHERE City = '{city}' AND State = '{state}';"
    elif city:
        query_sql += f" WHERE City = '{city}';"
    elif state:
        query_sql += f" WHERE State = '{state}';"
    return execute_query(query_sql)


# unwrapper(get_filtered_customers(state='SP', city='São Paulo'))


def count_customers_firstname() -> list:
    """
    Функция для вывода имен пользователей и количества их повторений.
    :return: List с именами и количеством повторов
    """
    query_sql = '''
        SELECT FirstName
          FROM customers
    '''
    query_result = execute_query(query_sql)
    all_names = query_result[0]
    for item in range(1, len(query_result)):
        all_names += query_result[item]

    name_and_count = []
    for item in all_names:
        counter = all_names.count(item)
        name = f'Name {item} repeats {counter} times'
        if name not in name_and_count:
            name_and_count.append(name)

    return name_and_count

print(count_customers_firstname())


def sum_of_orders():
    """
    Функция для подсчета общей стоимости заказов
    :return: Строка со значением
    """
    query_sql = '''     
    SELECT UnitPrice, Quantity
      FROM invoice_items
      '''
    query_result = execute_query(query_sql)
    multiplications = []
    for item in query_result:
        multiplications.append(item[0] * item[1])
    total_sum = round(sum(multiplications), 2)

    return f'Total amount of all orders - {total_sum}'

print(sum_of_orders())