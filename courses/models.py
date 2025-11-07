from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', default='course_thumbnails/download.jpg')
    level = models.CharField(max_length=50, default='Beginner')
    duration = models.CharField(max_length=50, default='30 minutes')
    prerequisite = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE , related_name='unlocks',)
    title_reward = models.CharField(blank=True, max_length=100, null=True, unique=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserTitle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='titles')
    title = models.CharField(max_length=100)
    awarded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'title')

    def __str__(self):
        return f"{self.user.username} - {self.title}"

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

class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({'Completed' if self.completed else 'In Progress'})"