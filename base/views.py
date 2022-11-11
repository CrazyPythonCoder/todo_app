from django.shortcuts import render, redirect
from .models import Task, TodoUser
from .forms import TaskForm

# Create your views here.
def home(request):
    # Tasks
    tasks = Task.objects.all()
    
    # Forms
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'tasks': tasks, 'form': form}
    
    return render(request, 'home.html', context)

# def create_task(request):
#     return render(request, 'create.html')