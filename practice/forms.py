from django.contrib.auth.models import User
from django import forms
from .models import Question, TestCases


class ContactForm(forms.Form):
    data = forms.CharField(label='data', max_length=100)


class AddQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'


class AddTestCaseForm(forms.ModelForm):

    class Meta:
        model = TestCases
        exclude = ('number',)
