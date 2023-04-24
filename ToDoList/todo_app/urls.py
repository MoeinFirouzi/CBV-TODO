from django.urls import path
from todo_app.views import IndexView, TaskListView

app_name = "todo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('tasks/', TaskListView.as_view(), name="tasks"),
]
