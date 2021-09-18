from tasks import replace_double_single_quotes,is_palindrome

def test_task_1():
    assert replace_double_single_quotes('"""""""') == "'''''''"
    assert replace_double_single_quotes("'''''''") == '"""""""'
    assert replace_double_single_quotes("''\"'EPAM''BEST''\"Company") == "\"\"\'\"EPAM\"\"BEST\"\"\'Company"

def test_task_2():
    list_polindrom = ['redivider', 'deified', 'civic', 'radar', 'level', 'rotor', 'kayak', 'reviver', 'racecar', 'madam', 'refer']
    for iter in list_polindrom:
        assert is_palindrome(iter) is True
    list_polindrom = ['EPAM', 'COMPANY', 'BEST', 'FOR', 'WORK']
    for iter in list_polindrom:
        assert is_palindrome(iter) is False