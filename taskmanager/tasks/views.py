from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        if title.strip() != "":
            Task.objects.create(title=title)
        return redirect('home')

    context = {'tasks': tasks}
    return render(request, 'home.html', context)

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

