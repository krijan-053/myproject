from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Student

"""
=> API stands for Application Programmable Interface
=> APIs are the services provided by third parties.
=> Here, we are building aur own APIs
=> APIs and SDK are sometimes used interchangeably.
=> Here we build Restful APIs

-----------What are restful APIs ?--------
=> Rest stands for Representational State Transfer
=> Restful APIs are one of the ways to communicate among multiple services.
=> In Restful APIs, we communicate between services using JSON data format.
=> DRF (Django RestFramework) is the library built on top of django to createRestful APIs
"""


def hello_world(request):
    return JsonResponse({
        "message": "Hello World"
    })


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "name": "Jan Snow",
            "age": 34,
            "address": "Pokhara"
        })


class UserListView(APIView):
    def get(self, *args, **kwargs):
        user = [
            {"name": "Jan Snow", "age": 34},
            {"name": "Snow Man", "age": 21},
            {"name": "Eren", "age": 20},
            {"name": "Jan", "age": 32}
        ]
        return Response(user)


class StudentView(APIView):
    def get(self, *args, **kwargs):
        student = Student.objects.get(name="Jack")
        return Response({
            "name": student.name,
            "age": student.age,
            "department": student.department,
            "classroom": student.classroom.name
        })


class StudentListView(APIView):
    def get(self, request, *args, **kwargs):
        students_list = []
        for student in Student.objects.all():
            student = {
                "name": student.name,
                "age": student.age,
                "department": student.department,
                "classroom": student.classroom.name if student.classroom else None
                }
            students_list.append(student)
        return Response(students_list)
