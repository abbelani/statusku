web: python myapp/manage.py collectstatic --noinput;
web: gunicorn statusku.wsgi -b 0.0.0.0:$PORT;
