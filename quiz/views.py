from django.shortcuts import render,redirect
from django.contrib import messages

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
    if(request.method=='POST'):
        try:
            q1 = request.POST['question0']
            q2 = request.POST['question1']
            q3 = request.POST['question2']
            q4 = request.POST['question3']
            q5 = request.POST['question4']
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
            messages.info(request,'your result is:%s'%count)
            return redirect('quiz')
        except:
            messages.info(request,'Attempt all questions please')
            return redirect('quiz')
    else:
        return render(request,'Experiments/quiz.html')

def references(request):
    return render(request,"Experiments/references.html")

def simulation(request):
    return render(request,"Experiments/simulation.html")

def theory(request):
    return render(request,"Experiments/theory.html")



def aimjs(request):
    return render(request,"introjs/aim.html")

def  procedurejs(request):
    return render(request,"introjs/procedure.html")

def quizjs(request):
    return render(request,"introjs/quiz.html")

def referencesjs(request):
    return render(request,"introjs/references.html")

def theoryjs(request):
    return render(request,"introjs/theory.html")
    
def simulationjs(request):
    return render(request,"introjs/simulation.html")


    
def aimjs1(request):
    return render(request,"stringfun/aim.html")

def  procedurejs1(request):
    return render(request,"stringfun/procedure.html")

def quizjs1(request):
    return render(request,"stringfun/quiz.html")

def referencesjs1(request):
    return render(request,"stringfun/references.html")

def theoryjs1(request):
    return render(request,"stringfun/theory.html")
    
def simulationjs1(request):
    return render(request,"stringfun/simulation.html")



    

def quizjs1(request):
    if(request.method=='POST'):
        try:
            q1 = request.POST['question0']
            q2 = request.POST['question1']
            q3 = request.POST['question2']
            q4 = request.POST['question3']
            q5 = request.POST['question4']
            count=0
            if(q1=='b'):
                count+=1
            if(q2=='c'):
                count+=1  
            if(q3=='d'):
                count+=1
            if(q4=='d'):
                count+=1
            if(q5=='b'):
                count+=1
            messages.info(request,'your result is:%s'%count)
            return redirect('quizjs1')
        except:
            messages.info(request,'Attempt all questions please')
            return redirect('quizjs1')
    else:
        return render(request,'stringfun/quiz.html')
