from django.urls import path
from .import views

urlpatterns=[
    path('',views.control,name='control'),
]