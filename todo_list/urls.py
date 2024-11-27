from django.urls import path

from todo_list.views import (
    HomePageView,
    TagListView,
)


app_name="todo-list"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tags", TagListView.as_view(), name="tags"),
]

