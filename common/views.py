from django.shortcuts import render

from courses.models import Course, UserCourseProgress


# Create your views here.
def home(request):
    courses = Course.objects.all()

    if request.user.is_authenticated:
        completed_courses = UserCourseProgress.objects.filter(user=request.user, completed=True)
        return render(request, 'common.html', {'courses': courses, 'completed_courses': completed_courses})

    return render(request, 'common.html', {'courses': courses})
