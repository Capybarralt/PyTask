from .services import with_connection


SQL_CREATE_NEW_PAYMENT = '''
    INSERT INTO payment (title, value, amount, date_p) VALUES (?, ?, ?, ?)
'''

SQL_UPDATE_PAYMENT = '''
    UPDATE payment SET
        title=?, value=?, amount=?, date_p=?
    WHERE id=?
'''

SQL_SELECT_ALL_PAYMENTS = '''
    SELECT
        id, title, value, amount, date_p
    FROM
        payment
'''


SQL_SELECT_PAYMENT_BY_ID = f'{SQL_SELECT_ALL_PAYMENTS} WHERE id=?'

SQL_SELECT_PAYMENT_PERIOD = f'{SQL_SELECT_ALL_PAYMENTS} WHERE date_p BETWEEN ? AND ?'

SQL_SELECT_PAYMENT_TOP = f'{SQL_SELECT_ALL_PAYMENTS} ORDER BY (value*amount) DESC LIMIT ?'



@with_connection()
def initialize(conn, creation_schema):
    """Инициализирует структуру базы данных"""
    with open(creation_schema) as f:
        conn.executescript(f.read())


@with_connection()
def create_payment(conn, title, value, amount, date_p):
    """Сохраняет новый платеж в БД и возвращает ее."""
    cursor = conn.execute(SQL_CREATE_NEW_PAYMENT, (title, value, amount, date_p))
    pk = cursor.lastrowid # последний сгенерированный первичный ключ
    conn.commit()
    return get_payment(pk)


@with_connection()
def update_payment(conn, pk, title, value, amount, date_p):
    """Обновляет платеж с указанным идентификатором в БД."""
    conn.execute(SQL_UPDATE_PAYMENT, (title, value, amount, date_p, pk))


@with_connection()
def get_payment(conn, pk):
    """
    Выбирает и возвращает из БД задачу с указанным уникальный идентификатором.
    """
    cursor = conn.execute(SQL_SELECT_PAYMENT_BY_ID, (pk,))
    return cursor.fetchone()

@with_connection()
def get_all_payment(conn):
    cursor = conn.execute(SQL_SELECT_ALL_PAYMENTS)
    result = cursor.fetchall()
    return result

@with_connection()
def get_payments_period(conn, start, end):
    cursor = conn.execute(SQL_SELECT_PAYMENT_PERIOD, (start, end))
    return cursor.fetchall()

@with_connection()
def get_top_payment(conn, num):
    cursor = conn.execute(SQL_SELECT_PAYMENT_TOP, (num,))
    result = cursor.fetchall()
    return result
