from rest_framework.serializers import ModelSerializer

from education import models


class CourseSerializer(ModelSerializer):
    class Meta:
        model = models.Course
        fields =  "__all__"


class LessonsSerializer(ModelSerializer):
    class Meta:
        model = models.Lesson
        fields =  "__all__"