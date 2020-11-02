release: python manage.py migrate --noinput
web: gunicorn -k eventlet -w 1 PenL_backend.wsgi:application --log-file - --log-level debug