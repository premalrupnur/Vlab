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
def answers(request):
    
    q1 = request.GET['question0']
    q2 = request.GET['question1']
    q3 = request.GET['question2']
    q4 = request.GET['question3']
    q5 = request.GET['question4']
    count=0
    if(q1=='a'):
        count+=1
    if(q2=='a'):
        count+=1  
    if(q3=='a'):
        count+=1
    if(q4=='b'):
        count+=1
    if(q5=='c'):
        count+=1

    return render(request,"Experiments/answers.html",{'count':count})

def references(request):
    return render(request,"Experiments/references.html")

def simulation(request):
    return render(request,"Experiments/simulation.html")

def theory(request):
    return render(request,"Experiments/theory.html")