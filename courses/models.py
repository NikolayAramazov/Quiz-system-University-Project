from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', default='static/course_thumbnails/download.jpg')
    level = models.CharField(max_length=50, default='Beginner')
    duration = models.CharField(max_length=50, default='30 minutes')

    def __str__(self):
        return self.title

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True)
    info = models.TextField(blank=True)
    prompt = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    class Meta:
        ordering = ['order']

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, blank=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'question')
