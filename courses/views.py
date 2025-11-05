import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm
from .models import Course, Question, UserAnswer, UserCourseProgress, UserTitle


def course_quiz_view(request, slug):
    course = get_object_or_404(Course, slug=slug)
    questions = course.questions.all()

    answers = {ua.question_id: ua for ua in UserAnswer.objects.filter(user=request.user, question__course=course)}

    context = {
        'course': course,
        'questions': questions,
        'answers': answers,
    }
    return render(request, 'courses/course_quiz.html', context)


def course_complete(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/complete_course.html', {'course': course})

def check_answer(request, question_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        answer = data.get('answer', '').strip()

        question = Question.objects.get(id=question_id)

        is_correct = (answer.lower() == question.correct_answer.lower())

        user_answer, created = UserAnswer.objects.update_or_create(
            user=request.user,
            question=question,
            defaults={
                'answer': answer,
                'is_correct': is_correct
            }
        )

        return JsonResponse({'correct': is_correct})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def complete_course_check(request, slug):
    course = get_object_or_404(Course, slug=slug)

    total_questions = course.questions.count()
    correct_answers = UserAnswer.objects.filter(
        user=request.user,
        question__course=course,
        is_correct=True,
    ).count()

    # If the user answered all questions correctly, mark the course as completed
    if correct_answers == total_questions and total_questions > 0:
        progress, _ = UserCourseProgress.objects.get_or_create(user=request.user, course=course)
        progress.completed = True
        progress.save()
        if course.title_reward and not UserTitle.objects.filter(user=request.user, title=course.title_reward).exists():
            UserTitle.objects.create(
                user=request.user,
                title=course.title_reward,
            )

        return redirect('courses:course_complete', slug=course.slug)

    else:
        # If not all answers are correct, redirect back to the quiz page
        return redirect('courses:course_quiz', slug=course.slug)


def view_courses(request):
    courses = Course.objects.all()
    query = request.GET.get('query', '')

    if request.method == 'GET' and  request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if query:
            courses = Course.objects.filter(title__icontains=query)
        else:
            courses = Course.objects.all()
        return render(request, 'courses/partial_course.html', {'courses': courses, 'query': query})

    form = SearchForm(request.GET)

    context = {
        'form': form,
        'courses': courses,
    }

    return render(request, 'courses/view_courses.html', context)
