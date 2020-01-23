def geometric_progression_generator(b, q):
    if b == 0:
        raise ArithmeticError('The first term is zero')
    if q == 0:
        raise ArithmeticError('The denominator is zero')

    yield b

    while 1:
        b = b * q
        yield b
