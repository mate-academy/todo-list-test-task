from django.shortcuts import render
from django.views import generic

from todo_list.models import ToDo, Tag


class HomePageView(generic.ListView):
    model = ToDo
    template_name = "todo_list/home.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tags.html"
