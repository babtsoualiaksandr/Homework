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
    assert SuperBird.__mro__

def test_singleton():
    p = Sun.inst()
    f = Sun.inst()
    assert p is f

def test_money():
    x = Money(10, "BYN")
    y = Money(11) # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    assert str(z + 3.11 * x + y * 0.8) == '34.30 EUR'

    lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    assert str(s)=='2835.43 BYN'

    assert Money(2.1,"BYN") == Money(1)
    assert Money(0.93,"EUR") > Money(0.99)
    assert Money(0.93,"EUR") != Money(0.99)
    assert not Money(0.93,"EUR") < Money(0.99)

def test_Pagination():
    pages = Pagination('Your beautiful text', 5)
    assert pages.page_count==4
    assert pages.item_count==19
    assert pages.count_items_on_page(0)==5
    assert pages.count_items_on_page(3)==4
    assert pages.count_items_on_page(4)=='Exception: Invalid index. Page is missing.'
    assert pages.find_page('Your')==[0]
    assert pages.find_page('e')==[1,3]
    assert pages.find_page('beautiful')==[1, 2]
    assert pages.find_page('great')=="Exception: 'great' is missing on the pages"
    assert pages.display_page(0)== 'Your '