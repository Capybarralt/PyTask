"""
todo: Модули

PYTHONPATH
"""

"""
todo: Как импортировать модуль?
"""

# todo: 1. Импорт модуля целиком

import sys
import input_utils

print(sys.path)

# a = input_utils.input_int()


# todo: 2. Частичный импорт

from input_utils import input_float, input_bin

# b = input_float()
# c = input_bin()


# todo: 3. Импорт со *

from input_utils import *


# todo: Как задать псевдоним?

from input_utils import user_input as base_user_input
import os.path as path



# import demo
#
# print(demo.is_debug())
# demo.debug = True
# print(demo.is_debug())

from demo import debug, is_debug

print(is_debug(), debug)
debug = True
print(is_debug(), debug)

from demo import lst, get

lst.append(1)
print(get())

lst = [1, 2, 3]
print(get())



"""
todo: Главный (исполняемый) модуль
"""









