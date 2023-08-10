from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Student, ClassRoom
from .serializers import ClassRoomSerializer, StudentModelSerializer

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


# class StudentView(APIView):
#     def get(self, *args, **kwargs):
#         student = Student.objects.get(name="Jack")
#         return Response({
#             "name": student.name,
#             "age": student.age,
#             "department": student.department,
#             "classroom": student.classroom.name
#         })


class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        student = Student.objects.get(id=26)
        return Response(student)


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


class ClassRoomView(APIView):
    def get(self, *args, **kwargs):
        classroom_id = kwargs['id']
        try:
            classroom = ClassRoom.objects.get(id=classroom_id)
        except:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)


class ClassRoomListCreateView(APIView):
    def get(self, *args, **kwargs):
        class_rooms = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(class_rooms, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ClassRoomSerializer(data=data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            ClassRoom.objects.create(name=name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Bad Request"
            }, status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        serializer = StudentModelSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        Student.objects.create(**validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentGenericView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentGenericCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["title"] = "Add Create Student"
        return context

    def list(self, request, *args, **kwargs):
        return (request)


class StudentRetriveView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentDeleteView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer



"""
Status Codes
200 = Successful Get Request
201 = Successful Post Requested,Successfully Created
204 =  No Content(used on deleting data from Server)

301 / 302 = Permanent and Temporary Redirection4
 
400 = Bad Request(Frontend  provided wrong data)
401 = Unauthorized Request
403 = Authenticated but not authorized (No Permission)
404 = Page Not Found
405 = Method Not Allowed

500 = Backend Server Error
502 = Bad Gateway

"""

"""
def get_serializers_context()
def create()
def update()
def retrieve()
def list()
def destroy()

"""
