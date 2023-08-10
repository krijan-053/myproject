from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import ClassRoomModelSerializer, StudentModelSerializer, StudentProfileSerializer, \
    ClassRoomSerializer
from myapp.models import ClassRoom, Student, StudentProfile
from .permissions import IsSuperAdmin


# Create your views here.

class ClassRoomViewSet(ModelViewSet):
    permission_classes = [IsSuperAdmin]
    serializer_class = ClassRoomModelSerializer
    """
    Here action are list, retrieve, update, destroy, partial_update, create,student
    """

    def get_permissions(self):
        if self.action == "create":
            return [IsSuperAdmin(), ]
        return [IsAuthenticated(), ]

    def get_queryset(self):
        # if self.request.user.is_superuser:
        #     return ClassRoom.objects.all()
        return ClassRoom.objects.all()

    def self_serializer_class(self):
        if self.action == "student":
            return StudentModelSerializer
        return ClassRoomModelSerializer

    @action(detail=True)
    def student(self, *args, **kwargs):
        classroom = self.get_object()
        students = Student.objects.filter(classroom=classroom)
        ser = self.get_serializer(students, many=True)
        return Response(ser.data)


class StudentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Student.objects.all()

    #serializer_class = StudentModelSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name", "department"]
    filterset_fields = ["department", "age"]

    def get_serializer_class(self):
        if self.action == "profile":
            return StudentProfileSerializer
        return StudentModelSerializer

    @action(detail=True)
    def profile(self, *args, **kwargs):
        student = self.get_object()
        try:
            profile = student.studentprofile
            ser = self.get_serializer(profile)
            return Response(ser.data)
        except:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)


class StudentProfileViewSet(ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
