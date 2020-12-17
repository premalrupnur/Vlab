from os import name
from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('index.html',views.index,name='index'),
    path('Objective.html',views.objective,name='objective'),
    path('Resources.html',views.resources,name='resource'),
    path('Experiments.html',views.experiment,name='experiment'),
    path('Experiments/aim.html',views.aim,name='aim'),
    path('Experiments/procedure.html',views.procedure,name='procedure'),
    path('Experiments/quiz.html',views.quiz,name='quiz'),
    path('Experiments/theory.html',views.theory,name='theory'),
    path('Experiments/references.html',views.references,name='references'),
    path('Experiments/simulation.html',views.simulation,name='simulation'),
    path('Experiments/answers',views.answers,name='answers'),


]