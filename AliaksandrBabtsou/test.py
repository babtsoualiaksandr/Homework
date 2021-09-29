from tasks import *
import pytest
import logging

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )



def test_file_context_task7_1():
    test_text = "test-data from test pytest"
    name_file = 'output.txt'
    with FileContex(name_file, "w") as f:
        f.write(test_text)
    with FileContex(name_file, mode="r") as f:
        print(f)
        read = f.read()
        print(read)
    assert read==test_text
    try:
        with FileContex(name_file, "w") as f:
            f.write(test_text)
            raise Exception('my Error')
    except Exception as ex:
        print(ex)
    with FileContex(name_file, mode="r+") as f:
        print(f)
        read = f.read()
        print(read)
    assert read==test_text 


def test_file_contex():
    test_text = "test-data from test pytest"
    name_file = 'output.txt'
    with file_contex(name_file, "w") as f:
        f.write(test_text)
    with file_contex(name_file, mode="r") as f:
        print(f)
        read = f.read()
        print(read)
    assert read==test_text
    try:
        with file_contex(name_file, "w") as f:
            f.write(test_text)
            raise Exception('my Error')
    except Exception as ex:
        print(ex)
    with file_contex(name_file, mode="r+") as f:
        print(f)
        read = f.read()
        print(read)
    assert read==test_text 



    

