from rest_framework import serializers
from ..models.log_route_action import LogRouteAction

class LogRouteActionSerializer(serializers.ModelSerializer):
    webRoute = serializers.CharField(source='web_route')
    apiRoute = serializers.CharField(source='api_route')
    functionCode = serializers.CharField(source='function_code')
    functionName = serializers.CharField(source='function_name')
    actionCode = serializers.CharField(source='action_code')
    actionName = serializers.CharField(source='action_name')
    jsonParamsRequired = serializers.CharField(source='json_params_required')
    serviceName = serializers.CharField(source='service_name')
    dateCreated = serializers.DateTimeField(source='date_created', required=False, allow_null=True)
    dateModified = serializers.DateTimeField(source='date_modified', required=False, allow_null=True)
    
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
        model = LogRouteAction
        fields = [
            'route_action_id',
            'webRoute',
            'apiRoute',
            'functionCode',
            'functionName',
            'actionCode',
            'actionName',
            'jsonParamsRequired',
            'serviceName',
            'dateCreated',
            'dateModified'
        ]