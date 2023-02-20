from django.urls import path
from .views import CeleryView

urlpatterns = [
    path('test', CeleryView.as_view({'get':'test'}), name='test'),
    path('getall', CeleryView.as_view({'get':'getall'}), name='getall'),
    path('write_log', CeleryView.as_view({'post':'write_log'}), name='write_log'),
]