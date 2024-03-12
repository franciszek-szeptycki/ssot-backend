from django.urls import path
from .views import *

urlpatterns = [
    path('', user_info, name='user_info'),
]