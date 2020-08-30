from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string
from .models import Question, User
from .utils import paginate
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm
from django.shortcuts import redirect




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
        user_id = request.session.get('user')
        if not user_id:
            return redirect('qa:login_url')
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_form.cleaned_data['question'] = question
            user = User.objects.get(id=user_id)
            answer_form.cleaned_data['author'] = user
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
        user_id = request.session.get('user')
        if not user_id:
            return redirect('qa:login_url')
        question_form = AskForm(request.POST)
        if question_form.is_valid():
            user = User.objects.get(id=user_id)
            question_form.cleaned_data['author'] = user
            question_created = question_form.save()
            url = question_created.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        question_form = AskForm()
    context = {'question_form': question_form, 'question_url': url}
    return render(request, 'create_question.html', context=context)


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            request.session.SESSION_COOKIE_NAME = get_random_string(length=32)
            request.session.set_expiry(432000)
            user = login_form.cleaned_data['user']
            request.session['user'] = user.id
            return HttpResponseRedirect('/')
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        user_creation_form = SignUpForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return login_view(request)
    else:
        user_creation_form = SignUpForm()
    context = {'user_creation_form': user_creation_form}
    return render(request, 'signup.html', context)
