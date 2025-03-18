from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField
                                        )
from education import models
from education.models import Lesson


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course.pk).count()

    lessons_of_course = SerializerMethodField()
    def get_lessons_of_course(self, course):
        return [lesson.name_lesson for lesson in Lesson.objects.filter(course=course).order_by('id')]


    class Meta:
        model = models.Course
        fields =  ["id",
                "course_name",
                "description",
                "image",
                "count_lessons",
                "lessons_of_course"
                ]

class LessonsSerializer(ModelSerializer):
    class Meta:
        model = models.Lesson
        fields =  "__all__"