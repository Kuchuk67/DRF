from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    last_name = None
    first_name = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='аватарка')
    city = models.CharField(max_length=100, verbose_name='город', blank=True)
    number_phone = models.CharField(max_length=20, verbose_name='телефон', blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email