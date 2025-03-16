"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path


from education.views import CourseViewSet, LessonListViewSet, LessonCreateViewSet, LessonUpdateViewSet, LessonRetrieveViewSet, LessonDestroyViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lessons/', LessonListViewSet.as_view()),
    path('lessons/create/', LessonCreateViewSet.as_view()),
    path('lessons/<int:pk>/update/>', LessonUpdateViewSet.as_view()),
    path('lessons/<int:pk>/', LessonRetrieveViewSet.as_view()),
    path('lessons/<int:pk>/delete/', LessonDestroyViewSet.as_view()),
]

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='user')
urlpatterns += router.urls



