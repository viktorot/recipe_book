.PHONY: migrate devsrv

migrate:
	python3 manage.py migrate

devsrv:
	python3 manage.py runserver 0.0.0.0:8000