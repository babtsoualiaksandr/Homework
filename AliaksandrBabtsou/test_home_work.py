from home_work import tuple_into_integer
from home_work import unique_dictionaries
from home_work import sort_dictionary_by_key
from home_work import len_str, count_character_frequency, unique_words_sorted, get_divisors_number
import pytest
def test_1_1():
    test_str = 'dmsbmnbsdn'
    assert len(test_str) == len_str(test_str)

def test_1_2():
    test_str = 123
    with pytest.raises(Exception) as e_info:
        len_str(test_str)

def test_2_1():
    assert count_character_frequency('Oh, it is python') == {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

def test_3_1():
    assert unique_words_sorted(['red', 'white', 'black', 'red', 'green', 'black']) == ['black', 'green', 'red', 'white']

def test_4_1():
    assert get_divisors_number(60) == {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

def test_5_1():
    assert sort_dictionary_by_key({1:'dasd',5:'fgfhg',2: 2}) == {1: 'dasd', 2: 2, 5: 'fgfhg'}
    assert sort_dictionary_by_key({'a':'dasd','c':'fgfhg','b': 2}) == {'a': 'dasd', 'b': 2, 'c': 'fgfhg'}

def test_6_1():
    assert unique_dictionaries([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S005', 'S002', 'S007', 'S001', 'S009'}

def test_7_1():
    assert tuple_into_integer((1,2,3,4,5)) == 12345

