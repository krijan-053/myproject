from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ClassRoomViewSet, StudentViewSet, StudentProfileViewSet

router = DefaultRouter()
router.register('classroom', ClassRoomViewSet, basename='classroom')
router.register('student', StudentViewSet, basename='student')
router.register('student-profile', StudentProfileViewSet, basename='student_profile')

urlpatterns = [
    path("login/", obtain_auth_token, name="api_login")
              ] + router.urls
