import functools
from types import resolve_bases
from typing import List
from collections import Counter
import string
import csv
import operator
import functools

__all__ = [
    'sort_in_file',
    'most_common_words',
    'get_top_performers',
    'enclosing_funcion_4_4',
    'enclosing_funcion_4_4_2',
    'enclosing_funcion_4_4_3',
    'sum_of_numbers',
    ]


def try_exc():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                result = func(*args, **kwargs)
            except Exception as e:
                print('An exception occurred', e)
                result = f'{func.__name__} {args}  Error{e}'
            return result
        return wrapper
    return decorator


@try_exc()
def sort_in_file(input_file: str, output_file: str, reverse: bool = False) -> None:
    """
    sort_in_file [Sort the names]

    [Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`.]

    :param input_file: [Open file]
    :type input_file: str
    :param output_file: [write file]
    :type output_file: str
    :param reverse: [reverse], defaults to False
    :type reverse: bool, optional
    """
    with open(input_file, 'r') as in_file:
        rows = in_file.readlines()
    with open(output_file, 'w') as out_file:
        out_file.write(''.join(str(line)
                       for line in sorted(rows, reverse=reverse)))

@try_exc()
def most_common_words(filepath: str, number_of_words: int = 3) -> List[str]:
    """
    most_common_words [search for most common words]

    [Implement a function which search for most common words in the file.]

    :param filepath: [filepath]
    :type filepath: [type]
    :param number_of_words: [description], defaults to 3
    :type number_of_words: int, optional
    """
    with open(filepath, 'r') as in_file:
        rows = in_file.readlines()

    txt = ''.join(rows).translate(str.maketrans('', '', string.punctuation))
    return list([name for (name, _) in Counter(txt.split()).most_common(number_of_words)])


def get_top_performers(file_path:str, number_of_top_students:int=5)-> List[str]:
    """
    get_top_performers [summary]

    [This file contains the student’s names, age and average mark. 1) Implement a function which receives file path and returns names of top performer students]

    :param file_path: [file_path]
    :type file_path: str
    :param number_of_top_students: [number_of_top_students], defaults to 5
    :type number_of_top_students: int, optional
    :return: [names of top performer students]
    :rtype: List[str]
    """
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        students= [(row['student name'],int(float(row['age'])),float(row['average mark'])) for row in reader]
    sorted_by_mark = list(sorted(students, key=operator.itemgetter(2)))
    sorted_by_age = list(sorted(students, key=operator.itemgetter(1)))
    

    with open('data/students_sort_byage.csv', 'w', newline='') as csvfile:
        fieldnames = ['student name', 'age', 'average mark']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in sorted_by_age[::-1]:
            writer.writerow({'student name': row[0], 'age': row[1], 'average mark': row[2]})
    
    return list([key for key, _, _ in sorted_by_mark[-number_of_top_students:]])


a = "I am global variable!"

def enclosing_funcion_4_4():
    a = "I am variable from enclosed function!"

    def inner_function():
        
        a = "I am local variable!"
        print(a)
    return inner_function



def enclosing_funcion_4_4_2():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        # a = "I am local variable!"
        print(a)
    return inner_function



def enclosing_funcion_4_4_3():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        a = "I am local variable!"
        print(a)
    return inner_function



def remember_result(fun):
    def decorator(*args, **kwargs):

        last_result = None
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            nonlocal last_result
            print(f'Last result = ', last_result)
            if all(isinstance(n, int) for n in args):
                result = 0
                for item in args:
                    result += item
                print(f"Current result = '{result}'")
            else:
                result =fun(*args, **kwargs)
            last_result = result
            return result
        return wrapper
    return decorator()



@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result



def call_once(fun):
    memo = {}
    def decorator():
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            if fun.__name__ in memo:
                return memo[fun.__name__]
            else:
                result =fun(*args, **kwargs)
                memo[fun.__name__]=result
            return result
        return wrapper
    return decorator()


@call_once
def sum_of_numbers(a, b):
    return a + b

if __name__ =='__main__':
    print(most_common_words('data/lorem_ipsum.txt'))
    print(get_top_performers("data/students.csv"))
    enclosing_funcion_4_4()()
    enclosing_funcion_4_4_2()()
    enclosing_funcion_4_4_3()()
    sum_of_numbers(2,4)
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)
    print(sum_of_numbers(856, 232))
