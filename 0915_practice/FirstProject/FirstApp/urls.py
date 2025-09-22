from django.urls import path
from .views import *

app_name="FirstApp"

urlpatterns = [
    path('', index, name='index'),
    path('api', api, name='api'),
]

