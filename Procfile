web: bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT djangoBase/settings.py
worker: bin/python djangoBase/manage.py celeryd -E -B --loglevel=INFO
