from django import forms
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
    question = forms.IntegerField()

    def clean_question(self):
        try:
            selected_question = Question.objects.get(id=self.cleaned_data['question'])
            self.cleaned_data['question'] = selected_question
        except ObjectDoesNotExist:
            raise ValidationError('The question you are trying to answer does not exist')
        return self.cleaned_data['question']

    def save(self):
        return Answer.objects.create(**self.cleaned_data)
