import psycopg2
from con_config import HOST, USER, PASSWORD, DB_NAME, PORT

try:
    # Подключение к базе данных
    connection = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME,
        port=PORT
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version()'
        )
        print(cursor.fetchone())


except Exception as ex:
    print('Ошибка с подключением к базе данных')
    print(ex)
finally:
    if connection:
        connection.close()
    print('Соединени с базой данных завершено')
