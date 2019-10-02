def bubble_sort(lst, desc=False):
    l = len(lst)
    if desc == False:
        max(lst, l)
    else:
        min(lst, l)
    return lst

# Сортирует по возрастанию
def max(lst, l):
    for i in range(l - 1):
        for j in range(l - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Сортирует по убыванию
def min(lst, l):
    for i in range(l - 1):
        for j in range(l - i - 1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

"""

Напишите функцию bubble_sort(lst, desc=False), которая принимает один
обязательный аргумент - список из чисел, выполняет сортировку списка методом
пузырька и возвращает получившийся список.

Аргумент desc задает порядок сортировки. Если он равен True, то функция
сортирует по убыванию, если он равен False, то - по возрастанию.

По умолчанию функция сортирует список по возрастанию.

(!) Запрещено использовать встроенные возможности языка для сортировки.

"""
