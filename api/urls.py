from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.getCourses, name='GetCourses'),
    path('courses/<int:id>', views.getCourse, name='GetCourse'),
]