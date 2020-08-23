from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question
from .utils import paginate

def test(request, *args, **kwargs):
    '''
    Basic test function.
    '''
    return HttpResponse('OK')

def new_questions_view(request):
    '''
    View for the question objects listed sorted by addition date desc
    '''
    new_questions = Question.objects.new()
    page = paginate(request, new_questions)
    context = {'questions': new_questions, 'page': page}
    return render(request, 'questions.html', context=context)

def popular_questions_view(request):
    '''
    View for the question objects listed sorted by popularity desc
    '''
    popular_questions = Question.objects.popular()
    page = paginate(request, popular_questions)
    context = {'questions': popular_questions, 'page': page}
    return render(request, 'questions.html', context=context)


def single_question_view(request, id):
    '''
    view function for the single question
    '''
    question = get_object_or_404(Question, id=id)
    context = {'question': question, 'answers': question.answers.all()}
    return render(request, 'single_question.html', context=context)