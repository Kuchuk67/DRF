# DRF

# Тестовые данные

```
python manage.py loaddata data_test\Course_fixture.json
python manage.py loaddata data_test\Lesson_fixture.json
python manage.py loaddata data_test\User_fixture.json
python manage.py loaddata data_test\Pay_fixture.json
```

## API эндпоинт вывода списка платежей
#### Примеры:
менять порядок сортировки по дате оплаты
фильтровать по пользователю
```
/api/pay?user=1
```
фильтровать по курсу или уроку
```
/api/pay?paid_course=1
/api/pay?paid_lesson=1
```
фильтровать по способу оплаты
```
/api/pay?payment_method=transfer
```
сортировка по дате 
```
/api/pay?ordering=-data_at
```





### Создана модель User
добавлены поля :телефон; город; аватарка

### Создана модель User
добавлены поля :название, превью, описание

### Создана модель User
добавлены поля :название, описание, превью, ссылка


## CRUD для моделей курса
с помощью ModelViewSet


## CRUD для моделей урока.
Для реализации CRUD используются Generic-классы.






python  -Xutf8 manage.py dumpdata education.Course --output data_test\Course_fixture.json --indent 4
python  -Xutf8 manage.py dumpdata education.Lesson --output data_test\Lesson_fixture.json --indent 4
python  -Xutf8 manage.py dumpdata users.CustomUser --output data_test\User_fixture.json --indent 4
python  -Xutf8 manage.py dumpdata users.Pay --output data_test\Pay_fixture.json --indent 4

