from django.db import models

class LogUser(models.Model):
    class Meta:
        db_table = 'mypt_ho_logs_user_behavior_logs'
    
    log_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    email = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    is_tin_pnc_emp = models.IntegerField()
    job_title = models.CharField(max_length=255)
    child_depart = models.CharField(max_length=100)
    agency = models.CharField(max_length=30)
    parent_depart = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)
    function_code = models.CharField(max_length=255)
    function_name = models.CharField(max_length=255)
    action_code = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255)
    service_name = models.CharField(max_length=100)
    web_browser = models.CharField(max_length=100)
    api_input = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)