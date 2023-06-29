from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import FirstView, ClassRoomView, ClassRoomTemplateView, StudentListView, StudentDetailView, \
    ClassRoomFormView, classroom_form, student_form, student_model_form

urlpatterns = [
    path("", FirstView.as_view(), name="first_view"),
    path("classroom-template/", ClassRoomTemplateView.as_view(), name="classroom_template_view"),
    path("student-list/", StudentListView.as_view(), name="student_list_view"),
    path("student-detail/<int:pk>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("classroom-django-form/", ClassRoomFormView.as_view(), name="classroom_django_form"),
    path("classroom-form/", classroom_form, name="classroom_form"),
    path("classroom-form/", classroom_form, name="classroom_form"),
    path("student-form/", student_form, name="student_form"),
    path("student-model-form/", student_model_form, name="student_model_form"),

    path("classroom/", login_required(ClassRoomView.as_view()), name="classroom_view")

]
