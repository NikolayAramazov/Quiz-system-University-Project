from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('course/<slug:slug>/', views.course_quiz_view, name='course_quiz'),  # Quiz page for course
    path('questions/<int:question_id>/check/', views.check_answer, name='check_answer'),  # Answer check
    path('<slug:slug>/complete/', views.complete_course_check, name='course_complete_check'),  # Completion check
    path('<slug:slug>/finished/', views.course_complete, name='course_complete'),  # Completion page
    path('view_courses', views.view_courses, name='view_courses'),  # Course list
]