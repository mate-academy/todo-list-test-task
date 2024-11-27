from django.shortcuts import render
from django.views import generic

from todo_list.models import ToDo


class HomePageView(generic.ListView):
    model = ToDo
    template_name = "todo_list/home.html"