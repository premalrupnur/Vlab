from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"typing.html")

def index(request):
    return render(request,"index.html")

def objective(request):
    return render(request,"Objective.html")

def resources(request):
    return render(request,"Resources.html")

def experiment(request):
    return render(request,"Experiments.html")

def aim(request):
    return render(request,"Experiments/aim.html")

def procedure(request):
    return render(request,"Experiments/procedure.html")

def quiz(request):
    return render(request,"Experiments/quiz.html")

def references(request):
    return render(request,"Experiments/references.html")

def simulation(request):
    return render(request,"Experiments/simulation.html")

def theory(request):
    return render(request,"Experiments/theory.html")