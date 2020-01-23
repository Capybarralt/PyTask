from textwrap import dedent
import sys
import pkg_resources

from terminaltables import SingleTable

from lesson_utils import (
    user_input, multi_line_input, input_datetime, input_int
)

from . import storage
from .services import make_menu


main_menu, main_menu_handler = make_menu()


def print_payment_data(payments):
    table_data = [
        ['ID', 'Наименование', 'Цена', 'Количество', 'Дата платежа']
    ]

    for payment in payments:
        table_data.append([
            payment['id'], payment['title'], payment['value'],
            payment['amount'], payment['date_p'].strftime('%d.%m.%Y')
        ])

    table = SingleTable(table_data)
    print(table.table)

def get_payment():
    """Запрашивает идентификатор платежа и возвращает ее из БД"""
    payment_id = input_int('Введите ID платежа', required=True)

    payment = storage.get_payment(payment_id)

    if payment is None:
        print(f'Платежа с "{payment_id}" не найдена.')

    return payment


def input_payment_data(payment=None):
    """Запрашивает от пользователя данные о платеже"""
    payment = dict(payment) if payment else {}
    data = {}

    data['title'] = user_input(
        'Название: ', payment.get('title'), required=True
    )

    data['value'] = input_int('Стоимость: ', payment.get('value'), required=False)

    data['amount'] = input_int('Количество: ', payment.get('amount'), required=False)

    data['date_p'] = input_datetime(
        '%d.%m.%Y', 'Дата платежа',
        default=payment.get('date_p'),
        required=True
    )

    return data


@main_menu('1', 'Добавить платеж')
def action_add_payment():
    """Добавить задачу"""
    data = input_payment_data()
    payment = storage.create_payment(**data)
    print(f'''Задача "{payment['title']}" успешно создана.''')


@main_menu('2', 'Отредактировать платеж')
def action_edit_payment():
    """Отредактировать задачу"""
    payment = get_payment()

    if payment is None:
        return

    data = input_payment_data(payment)
    storage.update_payment(payment['id'], **data)
    print(f'''Задача "{payment['title']}" успешно отредактирована.''')

@main_menu('3', 'Вывести все')
def action_show():
    print_payment_data(storage.get_all_payment())

def get_period():
    start = input_datetime('%d.%m.%Y', 'Начало периода ', required=True)
    end = input_datetime('%d.%m.%Y', 'Конец периода ', required=True)
    payment = storage.get_payments_period(start, end)
    return payment


@main_menu('3', 'Вывести все платежи за указанный период')
def action_show_period():
    payment = get_period()
    print_payment_data(payment)

@main_menu('4', 'Вывести топ самых крупных платежей')
def action_show_top_payments():
    """Вывести топ самых крупных платежей"""
    num = input_int('Введите количесвто: ', required=True)
    payments = storage.get_top_payment(num)

    print_payment_data(payments)

@main_menu('5', 'Вывести все')
def action_show_all():
    print_payment_data(storage.get_all_payment())

@main_menu('q', 'Выйти')
def action_exit():
    """Выйти"""
    sys.exit(0)


def main():
    schema_path = pkg_resources.resource_filename(__name__, 'resources/schema.sql')
    storage.initialize(schema_path)

    main_menu_handler('m')

    while 1:
        cmd = input('\nВведите команду: ')
        main_menu_handler(cmd)
