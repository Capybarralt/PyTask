def is_palindrome(s):
    if type(s) == int:
        s = str(s)

    dele = '!?.,<>/*-+=|\\@#№$;:^&_() '
    s = s.translate({ord(c): None for c in dele}) \
         .lower()

    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
        else:
            return True

"""

Напишите функцию is_palindrome(s), которая проверяет, является ли переданное
число или строка палиндромом и возвращает True. В противном случае возвращает
False.

Палиндром - это число или текст, который читается одинаково и слева, и справа,
пробелы, знаки пунктуации и регистр символов не учитываются.

"""
