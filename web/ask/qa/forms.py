from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Question, Answer


class AskForm(forms.Form):
    '''
    Form for adding questions.
    '''
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    '''
    Form for adding answers
    '''
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        return Answer.objects.create(**self.cleaned_data)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user_with_the_same_username = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if user_with_the_same_username:
            raise ValidationError('User with the same username already exists.')
        user_with_the_same_email = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if user_with_the_same_email:
            raise ValidationError('User with the same email already exists')
        return self.cleaned_data

    def save(self):
        return User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        print (user)
        if not user:
            raise ValidationError('Invalid username/password')
        self.cleaned_data['user'] = user
        return self.cleaned_data
