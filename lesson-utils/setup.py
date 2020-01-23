"""
name:             название пакета
version:          версия пакета

description:      Краткое описание
url:              URL-адрес пакета
license:          Лицензия (требуется верная запись)
author:           Имя автора
author_email:     E-Mail автора
packages:         Пакеты, которые нужно скопировать при установке
                  (без рекурсии, необходимо указать все вложенные пакеты)
py_modules:       Модули, которые нужно скопировать при установке
scripts:          Запускаемые из командной строки скрипты
install_requires: Прямые зависимости пакета от других пакетов
"""

from setuptools import setup

setup(
    name='lesson-utils',
    version='0.1.0',
    description='Collection of useful features for the course Python.',
    license='Apache License 2.0',
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    packages=['lesson_utils'],
    install_requires=[
        'appdirs',
    ]
)
