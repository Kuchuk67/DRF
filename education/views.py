from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from education.serializer import CourseSerializer, LessonSerializer
from users.models import CustomUser
from education.models import Course
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

# Create your views here.
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonCreateViewSet(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = LessonSerializer

class LessonListViewSet(ListAPIView):
        queryset = Course.objects.all()
        serializer_class = LessonSerializer

class LessonRetrieveViewSet(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = LessonSerializer

class LessonUpdateViewSet(UpdateAPIView):
        queryset = Course.objects.all()
        serializer_class = LessonSerializer

class LessonDestroyViewSet(DestroyAPIView):
        queryset = Course.objects.all()
        serializer_class = LessonSerializer




