from django.contrib import admin

# Register your models here.
# courses/admin.py
from django.contrib import admin
from .models import Course, Question, UserCourseProgress, UserAnswer, UserTitle


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [QuestionInline]

@admin.register(UserCourseProgress)
class UserCourseProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')

@admin.register(UserAnswer)
class UserAnswer(admin.ModelAdmin):
    list_display = ('user', 'answer')

@admin.register(UserTitle)
class UserTitle(admin.ModelAdmin):
    list_display = ('user', 'title')