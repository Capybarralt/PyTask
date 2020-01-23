"""
DRY
"""

from datetime import datetime


__all__ = (
    'user_input', 'input_int', 'input_float', 'input_bin',
    'confirm', 'multi_line_input',
    'input_datetime', 'input_date'
)


def user_input(msg='Введите значение', default=None,
               value_callback=None, trim_spaces=True,
               show_default=True, required=False):
    if show_default and default is not None:
        msg += f' [{default}]' # ' [{}]'.format(default)

    if default is not None:
        required = False

    while 1:
        value = input(f'{msg}: ')

        if trim_spaces:
            value = value.strip()

        if value:
            if value_callback is None:
                return value

            try:
                return value_callback(value)
            except ValueError as err:
                print(err)
        else:
            if not required:
                return default

            print('Требуется ввести значение')


def input_int(msg='Введите число', default=None, required=False):
    return user_input(
        msg, default, value_callback=int, required=required
    )


def input_float(msg='Введите число', default=None, required=False):
    return user_input(
        msg, default, value_callback=float, required=required
    )


def input_bin(msg='Введите число', default=None, required=False):
    """
    def to_bin(v):
        return int(v, 2)

    user_input(
        msg, default,
        value_callback=to_bin,
        required=required
    )
    """
    return user_input(
        msg, default,
        value_callback=lambda v: int(v, 2),
        required=required
    )


def confirm(msg='Подтвердите действие',
            default_yes=False, default_no=False, required=False):

    def callback(value):
        answers = {
            'y': True,
            'yes': True,
            'n': False,
            'no': False,
        }

        answer = answers.get(value.lower())

        if answer is None:
            valid_values = '/'.join(answers.keys())
            raise ValueError(f'Допустимые значения: {valid_values}')

        return answer

    if default_yes and default_no:
        raise RuntimeError('Оба аргумента default_yes и default_no заданы как True.')

    if default_yes:
        default = True
        msg += ' [Y/n]'
    elif default_no:
        default = False
        msg += ' [y/N]'
    else:
        default = None
        msg += ' [y/n]'

    return user_input(msg, default, value_callback=callback,
                      show_default=False, required=required)


def multi_line_input(msg='Введите текст', default=None):
    print(f'{msg}:')
    print('Ctrl+D/Ctrl+Z (Windows) для завершения ввода')

    if default is not None:
        print('[Оставьте поле пустым, чтобы использовать значение по умолчанию]')

    text = []

    while 1:
        try:
            value = input('> ')

            if not text and not value:
                return default

            text.append(value)
        except EOFError:
            print()
            return '\n'.join(text)


def input_datetime(fmt, msg='Введите дату', default=None, required=False):
    """
    Запрашивает дату и время от пользователя через STDIN в указанном формате и возвращает ее.

    Arguments:
        fmt (str): формат даты/времени, см. datetime.strftime()
        msg (str): строка приглашения.
        default: значение, которое будет использовано в случае пустого ввода.
    """
    if default is not None:
        msg += f' [{default:{fmt}}]'

    return user_input(
        msg,
        default,
        lambda value: datetime.strptime(value, fmt),
        required=required,
        show_default=False
    )


def input_date(fmt, msg='Введите дату', default=None, required=False):
    value = input_datetime(fmt, msg, default, required=required)

    if value is None:
        return value

    return value.date()













