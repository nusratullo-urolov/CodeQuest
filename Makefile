mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver

#9860 0301 9352 7477