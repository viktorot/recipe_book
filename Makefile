.PHONY: manage.py devsrv

devsrv:
	export SECRET_KEY=123; python3 manage.py runserver 127.0.0.1:8000

manage.py:
	export SECRET_KEY=123; python3 manage.py $(CMD)