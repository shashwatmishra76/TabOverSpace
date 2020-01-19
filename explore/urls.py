from django.urls import path
from . import views

app_name="explore"

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:subtopic>/', views.subtopic, name='subtopic'),
    path('<slug:subtopic>/<slug:article>/', views.article, name='article'),
]
