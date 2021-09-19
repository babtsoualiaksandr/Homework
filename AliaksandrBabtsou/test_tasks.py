from tasks import combine_dicts
from tasks import generate_squares
from tasks import alphabet_not_used
from tasks import appear_in_two
from tasks import appear_at_one
from tasks import appear_in_all
from tasks import get_pairs
from tasks import foo
from tasks import get_shortest_word
from tasks import get_digits
from tasks import split_by_index
from tasks import replace_double_single_quotes, is_palindrome, str_split


def test_task_1():
    assert replace_double_single_quotes('"""""""') == "'''''''"
    assert replace_double_single_quotes("'''''''") == '"""""""'
    assert replace_double_single_quotes(
        "''\"'EPAM''BEST''\"Company") == "\"\"\'\"EPAM\"\"BEST\"\"\'Company"


def test_task_2():
    list_polindrom = ['redivider', 'deified', 'civic', 'radar',
                      'level', 'rotor', 'kayak', 'reviver', 'racecar', 'madam', 'refer']
    for iter in list_polindrom:
        assert is_palindrome(iter) is True
    list_polindrom = ['EPAM', 'COMPANY', 'BEST', 'FOR', 'WORK']
    for iter in list_polindrom:
        assert is_palindrome(iter) is False


def test_task_3():
    text = 'Love the Python? Love the Python? Love the Python?  the Python?'
    assert text.split(sep=' ', maxsplit=3) == str_split(
        text, sep=' ', maxsplit=3)
    text = 'Love   the   Python?'
    assert text.split() == str_split(text)
    text = 'in Company EPAM, Love   the   Python?, in Company EPAM'
    assert text.split(',') == str_split(text, sep=',')


def test_task_4():
    assert split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == [
        "python", "is", "cool", ",", "isn't", "it?"]
    assert split_by_index("no luck", [42]) == ["no luck"]

def test_task_5():
    assert get_digits(87178291199)==(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

def test_task_6():
    assert get_shortest_word('Python is simple and effective!')=='effective!'
    assert get_shortest_word('Any pythonista like namespaces a lot.')=='pythonista'

def test_task_7():
    assert foo([1, 2, 3, 4, 5])==[120, 60, 40, 30, 24]
    assert foo([3, 2, 1])==[2, 3, 6]

def test_task_8():
    assert get_pairs([1, 2, 3, 8, 9])==[(1, 2), (2, 3), (3, 8), (8, 9)]

    assert get_pairs(['need', 'to', 'sleep', 'more'])==[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

    assert get_pairs([1]) is None

def test_task_9():
    test_strings = ["hello", "world", "python", ]
    assert appear_in_all(*test_strings)=={'o'}
    assert appear_at_one(*test_strings)=={'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
    assert appear_in_two(*test_strings)=={'h', 'l', 'o'}
    assert alphabet_not_used(*test_strings)=={'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}


def test_task_10():
    assert generate_squares(5)=={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def test_task_11():
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    assert combine_dicts(dict_1, dict_2)=={'a': 300, 'b': 200, 'c': 300}
    assert combine_dicts(dict_1, dict_2, dict_3)=={'a': 600, 'b': 200, 'c': 300, 'd': 100}