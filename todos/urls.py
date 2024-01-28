from django.urls import path
from todos import views
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView


urlpatterns = [
    path("todo_listw/", views.todo_list,),
    path("todo_list/", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]
