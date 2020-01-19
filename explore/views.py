from django.shortcuts import get_object_or_404, render

from .models import Subtopic, Article

# Create your views here.
def index(request):
    return subtopic(request, 'ai')

def get_subtopic(subtopic):
    if '_' in str(subtopic):
        sections = subtopic.split('_')
        sections = [section.capitalize() for section in sections]
        y = " ".join(sections)
        return y
    return subtopic.upper() if len(subtopic) == 2 else subtopic.capitalize()

def subtopic(request, subtopic):
    Subtopics = Subtopic.objects.all()

    section = get_object_or_404(Subtopic, name=get_subtopic(subtopic))
    context = {
    'section': section,
    'Subtopics': Subtopics,
    }
    return render(request, 'explore/index.html', context)

def article(request, subtopic, article):
    def get_article(article):
        sections = article.split(' ')
        sections = [section.lower() for section in sections]
        y = "_".join(sections)
        return y

    article = get_article(article)

    Subtopics = Subtopic.objects.all()

    section = get_object_or_404(Subtopic, name=get_subtopic(subtopic))
    context = {
    'section': section,
    'Subtopics': Subtopics,
    'article': article,
    }
    return render(request, 'explore/exp_article.html', context)
