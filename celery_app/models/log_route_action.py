from django.db import models

class LogRouteAction(models.Model):
    class Meta:
        db_table = 'mypt_ho_logs_routes_actions'
    
    route_action_id = models.AutoField(primary_key=True)
    web_route = models.CharField(max_length=255)
    api_route = models.CharField(max_length=255)
    function_code = models.CharField(max_length=255)
    function_name = models.CharField(max_length=255)
    action_code = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255)
    json_params_required = models.CharField(max_length=255)
    service_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)