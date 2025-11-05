from django.shortcuts import render

from courses.models import Course

def home(request):
    courses = Course.objects.all()

    if request.user.is_authenticated:
        completed_courses = Course.objects.filter(
            usercourseprogress__user=request.user,
            usercourseprogress__completed=True
        )
        completed_courses_ids = completed_courses.values_list('id', flat=True)
        context = {
            'courses': courses,
            'completed_courses': completed_courses,
            'completed_courses_ids': completed_courses_ids
        }
        return render(request, 'common.html', context)

    return render(request, 'common.html', {'courses': courses})