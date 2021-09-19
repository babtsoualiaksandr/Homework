from typing import Dict, List, Set, Tuple
from functools import reduce
import string 


def replace_double_single_quotes(input_string: str) -> str:
    def replace_char(ch: str) -> str:
        if ch == '"':
            return "'"
        if ch == "'":
            return '"'
        return ch
    return ''.join(list(map(replace_char, input_string)))


def is_palindrome(input_string: str) -> bool:
    return True if input_string == input_string[::-1] else False


def str_split(input_string: str, sep: str = ' ', maxsplit: int = -1) -> List[str]:
    result = []
    idx = 0
    idx_split = 0
    if maxsplit == -1:
        maxsplit = len(input_string)
    while idx <= len(input_string):
        if idx_split < maxsplit:
            idx_sep = input_string.find(sep, idx, len(input_string))
            if idx_sep == -1:
                result.append(input_string[idx:])
                idx_split += 1
                break
            word = input_string[idx:idx_sep]
            if word != '':
                result.append(word)
                idx_split += 1
            idx = idx_sep+1
        else:
            result.append(input_string[idx:])
            break
    return result


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    result = []
    idx_start = 0
    for idx_end in indexes:
        result.append(s[idx_start:idx_end])
        idx_start = idx_end
    print(idx_start)
    if idx_start < len(s):
        result.append(s[idx_start:])
    return result


def get_digits(num: int) -> Tuple[int]:
    return tuple(list([int(s) for s in str(num)]))


def get_shortest_word(s: str) -> str:
    words = s.split(' ')
    len_max = 0
    longest_word = ''
    for word in words:
        len_word = len(word)
        if len_word > len_max:
            len_max = len_word
            longest_word = word
    return longest_word


def foo(input_list_int: List[int]) -> List[int]:
    result = []
    for i in range(len(input_list_int)):
        list_int = input_list_int[:]
        list_int.pop(i)
        result.append(reduce(lambda el_prev, el: el_prev * el, list_int))
    return result

def get_pairs(lst: List) -> List[Tuple]:
    if len(lst)<2:
        return None
    return list([(lst[i], lst[i+1]) for i in range(len(lst)-1)])


def appear_in_all(*s)-> Set[str]:
    return reduce(lambda prev, next : prev & next,list([set(''.join(iter)) for iter in s]))



def appear_at_one(*s)-> Set[str]:
    return reduce(lambda prev, next : prev | next,list([set(''.join(iter)) for iter in s]))




def appear_in_two(*s)-> Set[str]:
    result = []
    list_s=list(s)
    for iter in s:
        list_s.remove(iter)
        pair=[iter, ''.join(list_s)]
        list_s=list(s)
        result.append(appear_in_all(*pair))
    return appear_at_one(*result)

def alphabet_not_used(*s)-> Set[str]:
    return set(string.ascii_lowercase) -set(''.join(s))


def generate_squares(num:int)-> dict:    
    return {i:i**2 for i in range(1,num+1)}




def combine_dicts(*args):
    def combine_two_dicts(dict1,dict2):
        result_dict = {**dict1, **dict2}
        for key, value in result_dict.items():
            if key in dict1 and key in dict2:
                    result_dict[key] = value + dict1[key]
        return result_dict
    return reduce(lambda prev, next : combine_two_dicts(prev, next),args)

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
combine_dicts(dict_1, dict_2, dict_3)



