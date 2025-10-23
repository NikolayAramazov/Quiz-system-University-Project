from django.contrib import admin

# Register your models here.
# courses/admin.py
from django.contrib import admin
from .models import Course, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [QuestionInline]
