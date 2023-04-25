from django.urls import path
from todo_app.views import IndexView, TaskListView, TaskDetailView,\
    TaskCreateView, TaskDeleteView

app_name = "todo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('tasks/', TaskListView.as_view(), name="tasks"),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('tasks/create/', TaskCreateView.as_view(), name="task_create"),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name="task_delete"),
]
