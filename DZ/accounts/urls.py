from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('courses/', views.courses, name="courses"),
    path('student/<str:pk>/', views.student, name="student"),
    path('register/', views.Register, name="register"),
]