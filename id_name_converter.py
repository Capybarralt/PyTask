def camel_to_snake(name):
    start = 0
    end = len(name)
    while start < end:
        if name[start].isupper():
            name = name.replace(name[start], '_' + name[start].lower())
            end = len(name)
        start += 1
    if name[0] == '_':
        name = name[1:]
    return name

def snake_to_camel(name):
    name = name.title() \
               .replace('_', '')
    return name

"""

Требуется реализовать две функции для конвертации имен идентификаторов.

Имя идентификатора в ЯП - это имена переменных, констант, функций, классов и т.д.

CamelCase (верблюжия нотация) - стиль написания составных слов, при котором
несколько слов пишутся слитно без пробелов, при этом каждое слово внутри фразы
пишется с заглавной буквы.

snake_case (змеиная нотация) - стиль написания составных слов, при котором
несколько слов разделяются символом подчеркивания (_), и не имеют пробелов
в записи, причём каждое слово пишется с маленькой буквы.

    Напишите функцию camel_to_snake(name), которая принимает в качестве
    единственного аргумента имя идентификатора в CamelCase нотации и
    возвращает его запись в змеиной нотации.

    Напишите функцию snake_to_camel(name), которая принимает в качестве
    единственного аргумента имя идентификатора в змеиной нотации и
    возвращает его запись в CamelCase нотации.

"""
