from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from education.models import Course, Lesson


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100,
                                verbose_name="Имя",
                                blank=True,
                                unique=False
                                )
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/',
                               blank=True,
                               verbose_name='аватарка'
                               )
    city = models.CharField(max_length=100,
                            verbose_name='город',
                            blank=True
                            )
    number_phone = models.CharField(max_length=20,
                                    verbose_name='телефон',
                                    blank=True
                                    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

STATUS_CHOICES = [
    ("cash", "Наличные"),
    ("transfer", "перевод на счет"),
]

class Pay(models.Model):
    user = models.ForeignKey(CustomUser,
                            null=False,
                            on_delete=models.CASCADE,
                            related_name="paid_lesson"
                            )

    data_at = models.DateTimeField(auto_now_add=True,
                                   verbose_name="дата оплаты"
                                   )

    paid_course = models.ForeignKey(Course,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    related_name="paid_course"
                                    )

    paid_lesson = models.ForeignKey(Lesson,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    related_name="paid_lesson"
                                    )

    summa_pay = models.IntegerField(null=False,
                                 blank=False,
                                 default=1,
                                 validators=[MinValueValidator(0)],
                                 verbose_name="сумма оплаты")

    payment_method = models.CharField(max_length=10,
                                      choices=STATUS_CHOICES,
                                      default="cash",
                                      verbose_name="способ оплаты")
    class Meta():
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
        ordering = ["-data_at"]

    def __str__(self):
        return self.data_at

