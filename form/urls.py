from django.urls import path
from .views import template_form


urlpatterns =[
    path("",template_form, name='template_form')
]