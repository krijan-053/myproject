from django.urls import path
from .views import home, index, view_name_Jon, view_name_Jane,view_name,json_view,students,page1,page2,student_detail
#from .views import *


urlpatterns = [
    path("name/jon/",view_name_Jon),
    path("name/jane/",view_name_Jane),
    path("get-name/<str:name>/",view_name), # Path Converter
    path('index/',index),
    path('students/',students,name="students"),
    path('student/<int:id>/',student_detail,name="student_detail"),
    path('json-view/',json_view),
    path("page1/",page1),
    path("page2/", page2),

    path('',home)
]