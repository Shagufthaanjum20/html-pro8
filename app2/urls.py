app_name='nothing'
from django.urls import path
from app2.views import *
urlpatterns=[
    path('new1/',new1,name='new1'),
    path('new2/',new2,name='new2'),
]