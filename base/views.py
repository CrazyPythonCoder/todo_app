from django.shortcuts import render
from .models import Task, TodoUser

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    
    return render(request, 'home.html', context)

def create_task(request):
    return render(request, 'create.html')