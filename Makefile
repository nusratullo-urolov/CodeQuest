mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver


celery:
	celery --app root worker --loglevel=info