# Chạy Celery worker
celery -A celery_project worker -l info -P eventlet &

# Chạy Django server
python manage.py runserver