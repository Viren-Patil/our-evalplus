

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])




METADATA = {}


def check(remove_vowels):
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('fedcba') == 'fdcb'
    assert remove_vowels('eeeee') == ''
    assert remove_vowels('acBAA') == 'cB'
    assert remove_vowels('EcBOO') == 'cB'
    assert remove_vowels('ybcd') == 'ybcd'

check(remove_vowels)