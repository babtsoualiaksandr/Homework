from tasks import *
import pytest


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


def test_task_6_1_2():
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    assert d.get_history()==["bar"]

def test_task_6_1_3():
    cipher = Cipher("crypto")
    assert cipher.encode("Hello world")=="Btggj vjmgp"
    assert cipher.decode("Fjedhc dn atidsn")=="Kojima is genius"  

def test_task_6_1_4_Bird():
    b = Bird("Any")
    assert b.walk()=="Any bird can walk"

def test_task_6_1_4_NonFlyingBird():
    p = NonFlyingBird("Penguin", "fish")
    assert p.swim()=="Penguin bird can swim"

    assert p.eat()=="It eats mostly fish"

    with pytest.raises(AttributeError) as excinfo:
        p.fly()
        assert "Penguin nobject has no attribute 'fly'" in str(excinfo.value)
    

#AttributeError: 'Penguin' object has no attribute 'fly'
def test_task_6_1_4_FlyingBird():
    c = FlyingBird("Canary")
    assert str(c)=="Canary can walk and fly"
    assert c.eat()=="It eats mostly grains"

def test_task_6_1_4_SuperBird():
    s = SuperBird("Gull")
    assert str(s)=="Gull can walk, swim and fly"
    assert s.eat()=="It eats fish"                
