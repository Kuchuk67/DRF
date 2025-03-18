from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField
                                        )
from education import models
from education.models import Lesson


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course.pk).count()

    class Meta:
        model = models.Course
        fields =  ["id",
                "course_name",
                "description",
                "image",
                "count_lessons"
                ]

class LessonsSerializer(ModelSerializer):
    class Meta:
        model = models.Lesson
        fields =  "__all__"