release: python manage.py collectstatic
release: python manage.py migrate
web: gunicorn PenL_backend.wsgi --log-file -