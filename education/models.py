from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=150,
                                   verbose_name='название курса'
                                   )
    description = models.TextField(verbose_name='описание',
                                   null=True,
                                   blank=True,
                                   )
    image = models.ImageField(upload_to='images_cat/',
                              null=True,
                              blank=True,
                              verbose_name='изображение'
                              )

    def __str__(self):
        return f'{self.course_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=150,
                                   verbose_name='название урока')
    description = models.TextField(verbose_name='описание',
                                   null=True,
                                   blank=True,
                                   )
    img_lesson  = models.ImageField(upload_to='images_cat/',
                                    null=True,
                                    blank=True,
                                    verbose_name='изображение'
                                    )
    link_video = models.URLField(max_length=256)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,
                               related_name='course_lesson'
                               )

    def __str__(self):
        return f'{self.name_lesson}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
