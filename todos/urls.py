from django.urls import path
from todos import views
from todos.views import TodoListView, TodoCreateView


urlpatterns = [
    path("todo_listw/", views.todo_list,),
    path("todo_list/", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
]
