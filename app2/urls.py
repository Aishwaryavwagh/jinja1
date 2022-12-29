from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('jinja2/',jinja2,name='jinja2'),
]