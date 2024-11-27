from django.urls import path

from todo_list.views import HomePageView


app_name="todo-list"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]

