from django.db import models

# Create your models here.
class LogUser(models.Model):
    class Meta:
        db_table = 'mypt_logs_user_behavior_logs'
    log_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    email = models.CharField(max_length=255)
    is_tin_pnc_emp = models.IntegerField()
    child_depart = models.CharField(max_length=100)
    agency = models.CharField(max_length=30)
    parent_depart = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)
    function_name = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    device_token = models.CharField(max_length=255)
    device_platform = models.CharField(max_length=20)
    app_version = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Test(models.Model):
    class Meta:
        db_table = 'test'
    
    id = models.BigAutoField(primary_key=True)
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)