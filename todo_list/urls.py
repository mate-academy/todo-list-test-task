from django.urls import path

from todo_list.views import (
    HomePageView,
    TagListView,
    tag_toggle,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)


app_name="todo-list"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tags", TagListView.as_view(), name="tags"),
    path("tags/<int:pk>/toggle/", tag_toggle, name="tag-toggle"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]

