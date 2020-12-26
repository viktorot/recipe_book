.PHONY: migrate devsrv

migrate:
	python3 manage.py migrate

devsrv:
	export SECRET_KEY=123; python3 manage.py runserver 127.0.0.1:8000