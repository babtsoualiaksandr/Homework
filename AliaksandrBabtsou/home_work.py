def len_str(in_str: str) -> int:
    """
    len_str [calculate the length]

    [calculate the length of a string without using the `len` function]

    :param in_str: [string]
    :type in_str: str
    :return: [len string]
    :rtype: int
    """
    if not isinstance(in_str, str):
        raise TypeError(f'type {in_str} not string')

    counter = 0
    while in_str[counter:]:
        counter += 1
    return counter


def count_character_frequency(input: str) -> dict:
    """
    count_haracter_frequency [count the number of characters (character frequency]

    [Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).]

    :param input: [input string]
    :type input: str
    :return: [dict {character: frequency}]
    :rtype: dict
    """
    if not isinstance(input, str):
        raise TypeError(f'type {input} not string')
    frequencies = {}
    for char in input.lower():
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def unique_words_sorted(input: list) -> list:
    """
    unique_words_sorted [prints the unique words in sorted form]

    [Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.]

    :param input: [comma separated sequence of words]
    :type input: list
    :return: [unique words in sorted form]
    :rtype: list
    """
    return sorted(list(set(input)))


def get_divisors_number(input: int)-> set:
    """
    get_divisors_number [divisors of that number]

    [https://en.wikipedia.org/wiki/Divisor divisors of that number]

    :param input: [number]
    :type input: int
    :return: [list divisors]
    :rtype: set[int]
    """
    return set([i for i in range(1, input + 1) if input % i == 0])


def sort_dictionary_by_key(input: dict)-> dict:
    """
    sort_dictionary_by_key [Python program to sort a dictionary by key]

    [Python program to sort a dictionary by key]

    :param input: [dict]
    :type input: dict
    :return: [dictionary sort by key]
    :rtype: dict
    """
    return {key: input[key] for key in sorted(input)}

def unique_dictionaries(input: list)-> set:
    """
    unique_dictionaries [all unique values of all dictionaries in list ]

    [Python program to print all unique values of all dictionaries in a list]

    :param input: [dictionaries in a list]
    :type input: list[dict]
    :return: [set unique val dictionaries ]
    :rtype: set
    """
    return set([iter_dict[key] for iter_dict in input for key in iter_dict])


def tuple_into_integer(input: tuple)-> int:
    """
    tuple_into_integer [convert a given tuple of positive integers]

    [Python function to convert a given tuple of positive integers into an integer]

    :param input: [tuple of positive integers]
    :type input: tuple
    :return: [integer]
    :rtype: int
    """
    return int(''.join(str(i) for i in input))



def print_multiplication_table(a = 2, b = 4, c = 3, d = 7)-> None:
    for j in range(a-1,b+1):
        for i in range(c-1,d+1):
            if (i==c-1) & (j==a-1):
                print('    ', end=' ')
            if (i!=c-1) & (j==a-1):
                print(f'{i:4}', end=' ')
            if (i==c-1) & (j!=a-1):
                print(f'{j:4}', end=' ')
            if (i!=c-1) & (j!=a-1):
                print(f'{i*j:4}', end=' ')            
        print()

print_multiplication_table()


