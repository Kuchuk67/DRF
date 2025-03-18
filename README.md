# DRF

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