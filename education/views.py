from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from education.serializer import CourseSerializer, LessonsSerializer
from users.models import CustomUser
from education.models import Course, Lesson
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

# Create your views here.
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonCreateViewSet(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonsSerializer

class LessonListViewSet(ListAPIView):
        queryset = Lesson.objects.all()
        serializer_class = LessonsSerializer

class LessonRetrieveViewSet(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonsSerializer

class LessonUpdateViewSet(UpdateAPIView):
        queryset = Lesson.objects.all()
        serializer_class = LessonsSerializer

class LessonDestroyViewSet(DestroyAPIView):
        queryset = Lesson.objects.all()
        serializer_class = LessonsSerializer




