from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


class HomePageView(generic.ListView):
    model = Task
    template_name = "todo_list/home.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tags.html"


def tag_toggle(request: HttpRequest, pk: int) -> HttpResponse:
    todo = Task.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect(reverse("todo-list:home"))


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["title"]
    success_url = reverse_lazy("todo-list:tags")

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["title"]
    success_url = reverse_lazy("todo-list:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = ["title"]
    success_url = reverse_lazy("todo-list:tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo-list:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo-list:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo-list:home")
