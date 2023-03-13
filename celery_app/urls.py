from django.urls import path
from .views.log_user_view import *

urlpatterns = [
    path('get-log-user', LogUserView.as_view({'get':'get_log_user'}), name='get_log_user'),
    path('post-log-user', LogUserView.as_view({'post':'post_log_user'}), name='post_log_user'),
]