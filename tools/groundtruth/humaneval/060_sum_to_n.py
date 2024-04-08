

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n + 1))




METADATA = {}


def check(sum_to_n):
    assert sum_to_n(1) == 1
    assert sum_to_n(6) == 21
    assert sum_to_n(11) == 66
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050

check(sum_to_n)