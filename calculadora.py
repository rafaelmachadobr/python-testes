from pip import main


def soma(x, y):
    """Soma x e y

    >>> soma(10, 20)
    30

    >>> soma(-1, 6)
    5

    >>> soma('10', 26)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float

    >>> soma(30, '13')
    Traceback (most recent call last):
    ...
    AssertionError: y precisa ser int ou float
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y

def subtrai(x, y):
    """Subtrai x e y
    
    >>> subtrai(10, 5)
    5

    >>> subtrai(4, 13)
    -9

    >>> subtrai('12', 7)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x - y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)