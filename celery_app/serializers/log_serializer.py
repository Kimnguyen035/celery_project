from rest_framework import serializers
from ..models.log_user import *

class LogUserSerializer(serializers.ModelSerializer):
    userId = serializers.CharField(source='user_id', required=False, allow_null=True)
    email = serializers.CharField(required=False, allow_null=True)
    fullName = serializers.CharField(source='full_name', required=False, allow_null=True)
    isTinPncEmployee = serializers.IntegerField(source='is_tin_pnc_emp', default=0)
    jobTitle = serializers.CharField(source='job_title', required=False, allow_null=True, allow_blank=True)
    childDepart = serializers.CharField(source='child_depart', required=False, allow_null=True, allow_blank=True)
    agency = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    parentDepart = serializers.CharField(source='parent_depart', required=False, allow_null=True, allow_blank=True)
    branch = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    functionCode = serializers.CharField(source='function_code')
    functionName = serializers.CharField(source='function_name')
    actionCode = serializers.CharField(source='action_code')
    actionName = serializers.CharField(source='action_name')
    serviceName = serializers.CharField(source='service_name')
    webBrowser = serializers.CharField(source='web_browser', required=False, allow_null=True, allow_blank=True)
    apiInput = serializers.CharField(source='api_input', required=False, allow_null=True, allow_blank=True)
    dateCreated = serializers.DateTimeField(source='date_created', required=False, allow_null=True)
    dateModify = serializers.DateTimeField(source='date_modified', required=False, allow_null=True)
    
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        not_fields = kwargs.pop('not_fields', None)
        super().__init__(*args, **kwargs)
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
        fields = [
            'log_id',
            'userId',
            'email',
            'fullName',
            'isTinPncEmployee',
            'jobTitle',
            'childDepart',
            'agency',
            'parentDepart',
            'branch',
            'functionCode',
            'functionName',
            'actionCode',
            'actionName',
            'serviceName',
            'webBrowser',
            'apiInput',
            'dateCreated',
            'dateModify',
        ]