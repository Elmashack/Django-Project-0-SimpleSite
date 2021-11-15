from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'My new main page', 'key_task': tasks})

def about(request):
    return render(request, 'main/about.html')
def goal(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = "Text is incorrect"

    form = TaskForm()
    context = {
        'key_form': form,
        'err': error
    }
    return render(request, 'main/goal.html', context)

