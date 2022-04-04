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
    path('Experiments/quiz',views.quiz,name='quiz'),
    path('Experiments/theory.html',views.theory,name='theory'),
    path('Experiments/references.html',views.references,name='references'),
    path('Experiments/simulation.html',views.simulation,name='simulation'),
    path('introjs/aim.html',views.aimjs,name='aim'),
    path('introjs/procedure.html',views.procedurejs,name='procedure'),
    path('introjs/quiz',views.quizjs,name='quiz'),
    path('introjs/theory.html',views.theoryjs,name='theory'),
    path('introjs/references.html',views.referencesjs,name='references'),
    path('introjs/simulation.html',views.simulationjs,name='simulation'),
    path('stringfun/aim.html',views.aimjs1,name='aim'),
    path('stringfun/procedure.html',views.procedurejs1,name='procedure'),
  
    path('stringfun/theory.html',views.theoryjs1,name='theory'),
    path('stringfun/references.html',views.referencesjs1,name='references'),
    path('stringfun/simulation.html',views.simulationjs1,name='simulation'),
     
    path('stringfun/quiz.html',views.quizjs1,name='quiz'),
  

]