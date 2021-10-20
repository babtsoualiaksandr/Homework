docker-compose run .
python manage.py migrate&& python manage.py createsuperuser&&python manage.py crontab add

http://localhost:8000

swagger DOC
(http://localhost:8000/openapi)


http -a admin:admin POST http://127.0.0.1:8000/feeds/ 

'''
pytest -vv --cov=src
======================================================== test session starts ========================================================
platform darwin -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0 -- /Users/alexander/Documents/Python_Epam/Homework/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/alexander/Documents/Python_Epam/Homework/AliaksandrBabtsou/rss_reader
plugins: cov-2.12.1
collected 9 items                                                                                                                   

tests/test_rss_reader.py::test_format_output PASSED                                                                           [ 11%]
tests/test_rss_reader.py::test_local_storage PASSED                                                                           [ 22%]
tests/test_rss_reader.py::test_models PASSED                                                                                  [ 33%]
tests/test_rss_reader.py::test_parse_args PASSED                                                                              [ 44%]
tests/test_rss_reader.py::test_get_version PASSED                                                                             [ 55%]
tests/test_rss_reader.py::test_read_rss PASSED                                                                                [ 66%]
tests/test_rss_reader.py::test_parse_xml PASSED                                                                               [ 77%]
tests/test_rss_reader.py::test_get_rows_from_text PASSED                                                                      [ 88%]
tests/test_rss_reader.py::test_service_api PASSED                                                                             [100%]


---------- coverage: platform darwin, python 3.9.6-final-0 -----------
Name                   Stmts   Miss  Cover
------------------------------------------
src/__init__.py            0      0   100%
src/local_storage.py      60     45    25%
src/log.py                20      0   100%
src/models.py             16      0   100%
src/parser_xml.py         66      3    95%
src/pdf.py                64      3    95%
src/print_to_html.py      34      9    74%
src/rss_reader.py         80     30    62%
src/service_api.py        18      2    89%
src/utilits.py            81     31    62%
------------------------------------------
TOTAL                    439    123    72%
'''