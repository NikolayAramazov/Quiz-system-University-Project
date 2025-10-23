import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Course, Question, UserAnswer

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