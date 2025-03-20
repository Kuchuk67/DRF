# Generated by Django 5.1.7 on 2025-03-18 13:48

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_lesson_course'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_at', models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')),
                ('summa_pay', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'перевод на счет')], default='cash', max_length=10, verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paid_course', to='education.course')),
                ('paid_lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paid_lesson', to='education.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paid_lesson', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
                'ordering': ['-data_at'],
            },
        ),
    ]
