from tasks import *


def test_task_6_1_1():
    c = Counter(start=42)
    c.increment()
    c.get()
    assert c.get()==43
    c = Counter()
    c.increment()
    assert c.get()==1
    c.increment()
    assert c.get()==2
    c = Counter(start=42, stop=43)
    c.increment()
    assert c.get() == 43
    assert c.increment() == 'Maximal value is reached.'
    assert c.get() == 43
                                                    
