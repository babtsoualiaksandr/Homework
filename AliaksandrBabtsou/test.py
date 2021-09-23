from tasks import *


print(most_common_words('data/lorem_ipsum.txt'))

def test_task_4_2():
    assert most_common_words('data/lorem_ipsum.txt', number_of_words=3)==['donec', 'etiam', 'aliquam']

def test_task_4_3():
    assert get_top_performers("data/students.csv", 5) == ['Jessica Dubose', 'Heather Garcia', 'Teresa Jones', 'Richard Snider', 'Josephina Medina']
                                                      
