from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField
                                        )
from users.models import Pay, CustomUser
from education.models import Lesson, Course


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email"]

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["name_lesson"]

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["course_name"]

class PayProfileSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["data_at",
                  "summa_pay"]

class PaySerializer(ModelSerializer):

    user = UserSerializer()
    paid_course = CourseSerializer()
    paid_lesson = LessonSerializer()

    class Meta:
        model = Pay
        fields =  ["id",
                "user",
                "data_at",
                "paid_course",
                "paid_lesson",
                "summa_pay",
                "payment_method"
                ]

class CustomUserProfileSerializer(ModelSerializer):
    pay = SerializerMethodField()
    def get_pay(self, user):
        return [{"дата":pay_item.data_at,
                 "сумма":pay_item.summa_pay
                 } for pay_item in Pay.objects.filter(user=user).order_by('id')]

    class Meta:
        model = CustomUser
        fields = ["username",
                  "email",
                  "city",
                  "number_phone",
                  "pay"
                  ]

