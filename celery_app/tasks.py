from celery import shared_task
from .serializers.log_serializer import *

@shared_task
def add_log(value):
    test = LogUserSerializer(data=value)
    if not test.is_valid():
        return 'loi roi'
    test.save()
    return 'success'