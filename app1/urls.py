from django.urls import path
app_name='something'
from app1.views import *

urlpatterns=[
    path('html/',html,name='html'),
    path('html_response/',html_response,name='html_response'),
]