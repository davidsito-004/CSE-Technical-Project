from django.urls import path
from .views import get_headers, home

urlpatterns = [
    path('', home, name='headers-home'),
    path('get-headers/', get_headers, name='headers')
]
