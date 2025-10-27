import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, UserAnswer, UserCourseProgress


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

def check_answer(request, question_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        answer = data.get('answer', '').strip()

        question = Question.objects.get(id=question_id)

        is_correct = (answer.lower() == question.correct_answer.lower())

        return JsonResponse({'correct': is_correct})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def complete_course_check(request, slug):
    course = get_object_or_404(Course, slug=slug)

    total_questions = course.questions.count()
    correct_answers = UserAnswer.objects.filter(
        user=request.user,
        question__course=course,
        is_correct=True
    ).count()

    if correct_answers == total_questions and total_questions > 0:
        progress, _ = UserCourseProgress.objects.get_or_create(user=request.user, course=course)
        progress.completed = True
        progress.save()
        return redirect('course_complete', slug=course.slug)
    else:
        return redirect('course_quiz', slug=course.slug)


def course_complete(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/complete_course.html', {'course': course})