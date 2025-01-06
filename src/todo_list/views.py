from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm, TagForm

def home(request):
    todo_list = Task.objects.all().order_by('is_done', '-created_at')
    return render(request, 'todo_list/home.html', {'todo_list': todo_list})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'todo_list/tag_list.html', {'tags': tags})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'todo_list/add_task.html', {'form': form})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'todo_list/add_tag.html', {'form': form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_list/add_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('home')

def update_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'todo_list/add_tag.html', {'form': form})

def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect('tag_list')
