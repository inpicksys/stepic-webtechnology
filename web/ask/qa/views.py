from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question
from .utils import paginate
from .forms import AskForm, AnswerForm


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


def single_question_view(request, question_id):
    '''
    View function for single question
    '''
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        answer_form = AnswerForm(initial={'question': question.id})
    context = {'question': question, 'answers': question.answer_set.all(), 'answer_form': answer_form}
    return render(request, 'single_question.html', context=context)


def create_question_view(request):
    url = ''
    if request.method == 'POST':
        question_form = AskForm(request.POST)
        if question_form.is_valid():
            question_created = question_form.save()
            url = question_created.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        question_form = AskForm()
    context = {'question_form': question_form, 'question_url': url}
    return render(request, 'create_question.html', context=context)
