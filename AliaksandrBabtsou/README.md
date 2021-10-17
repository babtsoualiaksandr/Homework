docker-compose run .
python manager.py migrate
python manage.py createsuperuser

http://localhost:8000

swagger DOC
(http://localhost:8000/openapi)


http -a admin:admin POST http://127.0.0.1:8000/feeds/ 
