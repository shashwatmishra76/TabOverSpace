from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from .models import Track, Subdomain, Question, TestCases
from .forms import AddQuestionForm, AddTestCaseForm

import requests, json

# Create your views here.
def index(request):
    return render(request, 'practice/index.html', {})

def subdomain(request, track, subdomain):
    def section(x):
        if '_' in str(x):
            sections = x.split('_')
            y = sections[0].capitalize() + " " + sections[1].capitalize()
            return y
        return x.capitalize()

    Subdomains = Subdomain.objects.all()

    section = get_object_or_404(Subdomain, name=section(subdomain), track__name=section(track))
    context = {
    'section': section,
    'Subdomains': Subdomains,
    'track': track,
    }
    return render(request, 'practice/subdomain.html', context)

def question(request, subdomain, question, track):
    def question_name(x):
        if '_' in str(x):
            sections = x.split('_')
            y = ""
            for i in sections:
                y += i.capitalize() + " "
            return y
        return x.capitalize()

    question = question_name(question)

    def section(x):
        if '_' in str(x):
            sections = x.split('_')
            y = sections[0].capitalize() + " " + sections[1].capitalize()
            return y
        return x.capitalize()

    Subdomains = Subdomain.objects.all()

    section = get_object_or_404(Subdomain, name=section(subdomain), track__name=section(track))
    context = {
    'section': section,
    'Subdomains': Subdomains,
    'track': track,
    'question': question,
    }

    if request.method == "POST":
        username = request.POST['username']
        if username is not None:
            url = 'https://api.jdoodle.com/v1/execute'

            # API credentials are globally visible. Needs to be changed before
            # deploying
            params = {
                'script': username,
                'language': 'python3',
                'versionIndex': '1',
                'clientId': '3265e3f531417e92189918053074fb26',
                'clientSecret': '8dfde96ed1da61c9f8197b6b01933e164ba5569af54efc182dfd510b26322880'
            }

            query = jdoodle(url, params)

            context['query'] = query['output']

            return render(request, 'practice/question.html', context)

    return render(request, 'practice/question.html', context)


def jdoodle(url, params):
    response = requests.get(url, json=params)

    if response.status_code == 200:
        return json.loads(response.text)
    return {'output': 'Failure'}


class AddQuestion(CreateView):
    form_class = AddQuestionForm
    template_name = 'practice/add_model_data.html'
    success_url = reverse_lazy('practice:add_question')


class AddTestCase(FormView):
    form_class = AddTestCaseForm
    template_name = 'practice/add_model_data.html'

    def form_valid(self, form):
        data = form.cleaned_data
        existing_cases = TestCases.objects.filter(question_id=data[
            'question_id']).count()
        TestCases.objects.create(
            question_id=data['question_id'],
            number=existing_cases + 1,
            input=data['input'],
            output=data['output']
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('practice:add_test_case')
