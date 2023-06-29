from django.urls import path
from .views import home, classroom, classroom_delete, add_student, detail_student, student_delete, student_update

urlpatterns = [
    path("classroom-delete/<int:id>/", classroom_delete, name="classroom_delete"),
    path("add-student/", add_student, name="add_student"),
    path("detail-student/<int:id>/", detail_student, name="detail_student"),
    path("student-delete/<int:id>/", student_delete, name="crud_student_delete"),
    path("student-update/<int:id>/", student_update, name="student_update"),
    path("classroom/", classroom, name="crud_classroom"),
    path("", home, name="crud_home"),
]
