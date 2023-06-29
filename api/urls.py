from django.urls import path
from .views import hello_world, UserView,StudentView,UserListView,StudentListView

urlpatterns = [
    path("student/",StudentView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("user-list/", UserListView.as_view()),
    path("user/", UserView.as_view()),
    path("hello-world/", hello_world),
]
