from django.shortcuts import render, redirect
from finance_app.models import Task
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password) # this is done on the User data table 
        print(user, username, password)
        if user is not None:
            login(request, user)
            return redirect('home')
            
    return render(request, 'login.html')       
            
def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username= username, email=email, password = password)
        user.save()
        
        return redirect('login')
    return render(request, 'reg.html')     

@login_required   
def home(request):
    if request.method == 'POST':
        Item_name = request.POST.get('Item_name')
        description = request.POST.get('description')
        Amount = request.POST.get('Amount')
        Date_of_purchase = request.POST.get('Date_of_purchase')

        task = Task(user=request.user, Item_name= Item_name, description=description, Amount =Amount, Date_of_purchase=Date_of_purchase)
        task.save()
        
        return redirect('task')
    return render(request, 'home.html')

@login_required
def taskDisplay(request):
    # task = Task.objects.all()
    task = Task.objects.filter(user=request.user)
    
    return render(request, 'taskdisplay.html',{'task':task})

@login_required
def taskUpdate(request, id):
    task = Task.objects.get(pk = id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task')

@login_required
def taskDelete(request, id): 
    task = Task.objects.get(pk = id, user=request.user)
    task.delete()
    return redirect('task')