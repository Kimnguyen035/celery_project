from rest_framework.serializers import *
from configs.global_variable import *
import json


class DatetimeValidate(Serializer):
    startDate = DateField(required=True, format=DATETIME_FORMAT, input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'])
    endDate = DateField(required=True, format=DATETIME_FORMAT, input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'])
    
class InputValidate(Serializer):
    actionRoute = ListField()
    data = DictField()
    str_json_param_required = CharField(required=False)
    
    def validate(self, value):
        for actionData in value['actionRoute']:
            data_check = json.loads(actionData['jsonParamsRequired'])
            key = list(data_check.keys())
            if key[0] in value['data'].keys():
                if data_check[key[0]] == value['data'][key[0]]:
                    value['str_json_param_required'] = actionData['jsonParamsRequired']
                    break
            if key[0] not in value['data'].keys() and data_check[key[0]] == '':
                value['str_json_param_required'] = actionData['jsonParamsRequired']
                break
        return value