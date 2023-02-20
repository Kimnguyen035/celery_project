from celery import shared_task
from .serializer import *

@shared_task
def add_log(value):
    test = TestSerializer(data=value, many=True)
    if not test.is_valid():
        return 'loi roi'
    test.save()
    return 'success'