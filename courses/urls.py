from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('course/<slug:slug>/', views.course_quiz_view, name='course_quiz'),
    path('questions/<int:question_id>/check/', views.check_answer, name='check_answer'),
]
