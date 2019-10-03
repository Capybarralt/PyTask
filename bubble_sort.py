def bubble_sort(lst, desc = False):
    if ( not desc ):
        for i in range(len(lst)-1):
            for j in range(len(lst)-i-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j];
    else:
        for i in range(len(lst)-1):
            for j in range(len(lst)-i-1):
                if lst[j] < lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j];
    return lst;


"""

Напишите функцию bubble_sort(lst, desc=False), которая принимает один
обязательный аргумент - список из чисел, выполняет сортировку списка методом
пузырька и возвращает получившийся список.

Аргумент desc задает порядок сортировки. Если он равен True, то функция
сортирует по убыванию, если он равен False, то - по возрастанию.

По умолчанию функция сортирует список по возрастанию.

(!) Запрещено использовать встроенные возможности языка для сортировки.

"""
