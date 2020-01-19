from django.urls import path
from . import views

app_name="practice"

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:track>/<slug:subdomain>/', views.subdomain, name='subdomain'),
    path('<slug:track>/<slug:subdomain>/<slug:question>', views.question, name='question'),
    path('add/question', views.AddQuestion.as_view(), name='add_question'),
    path('add/test_case', views.AddTestCase.as_view(), name='add_test_case'),
]
