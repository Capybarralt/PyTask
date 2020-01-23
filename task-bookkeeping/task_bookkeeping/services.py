from configparser import ConfigParser
import sqlite3
import os
import pkg_resources
import shutil
from collections import namedtuple, OrderedDict

from lesson_utils.app_utils import get_config_dir, get_data_dir


def make_config(*config_files):
    config = ConfigParser()
    config.read(config_files)
    return config


def make_default_config():
    filename = os.path.join(
        get_config_dir(__package__), # !!!!
        'config.ini'
    )

    if not os.path.exists(filename):
        default = pkg_resources.resource_filename(__name__, 'resources/config.ini')
        shutil.copyfile(default, filename)

    return make_config(filename)


config = make_default_config()


def make_connection(name='db'):
    """Возвращает объект-подключения к БД SQLite"""
    db_name = os.path.join(
        get_data_dir(__package__), #!!!!
        config.get(name, 'db_name')
    )

    conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row

    return conn


def with_connection(name='db'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with make_connection(name) as conn:
                return func(conn, *args, **kwargs)
        return wrapper
    return decorator


def make_menu():
    actions = OrderedDict()
    Action = namedtuple('Action', ('func', 'title'))

    def action(cmd, title):
        def decorator(func):
            actions[cmd] = Action(func, title)
            return func
        return decorator

    def handler(cmd):
        action = actions.get(cmd)

        if action:
            action.func()
        else:
            print('Не известная команда')

    @action('m', 'Показать меню')
    def action_show_menu():
        for cmd, action in sorted(actions.items()):
            print(f'{cmd}. {action.title}')

    return action, handler


















