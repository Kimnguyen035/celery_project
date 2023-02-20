from rest_framework import serializers
from .models import *

class LogUserSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        not_fields = kwargs.pop('not_fields', None)
        super().__init__(*args, **kwargs)
        list_key = list(self.get_fields().keys())
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if not_fields is not None:
            for item in not_fields:
                self.fields.pop(item)
    
    class Meta:
        model = LogUser
        fields = '__all__'
        # fields = [
        #     'log_id',
        #     'user_id',
        #     'email',
        #     'is_tin_pnc_emp',
        #     'child_depart',
        #     'agency',
        #     'parent_depart',
        #     'branch',
        #     'function_name',
        #     'action_name',
        #     'device_id',
        #     'device_name',
        #     'device_token',
        #     'device_platform',
        #     'app_version',
        #     'date_created',
        #     'date_modified',
        # ]
        
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'