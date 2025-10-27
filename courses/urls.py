from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('course/<slug:slug>/', views.course_quiz_view, name='course_quiz'),
    path('questions/<int:question_id>/check/', views.check_answer, name='check_answer'),
    path('courses/<slug:slug>/complete/', views.complete_course_check, name='course_complete_check'),
    path('courses/<slug:slug>/finished/', views.course_complete, name='course_complete'),

]
