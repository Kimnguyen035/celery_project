from rest_framework.serializers import *
from configs.global_variable import *


class DatetimeValidate(Serializer):
    startDate = DateField(required=True, format=DATETIME_FORMAT, input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'])
    endDate = DateField(required=True, format=DATETIME_FORMAT, input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'])