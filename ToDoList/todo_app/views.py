from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from todo_app.models import Task


class IndexView(LoginRequiredMixin, TemplateView):
    """
    A simple view for testing
    """
    template_name = "todo_app/index.html"


class TaskListView(ListView):
    """
    This class represents a view that displays a list of tasks owned
    by the current user.

    Attributes:
        template_name (str): The name of the HTML template used to
        render the view.
        context_object_name (str): The name of the variable used to
        store the list of tasks in the context.

    Methods:
        get_queryset(): Returns a queryset of tasks owned by the
        current user.
    """
    template_name = "todo_app/tasks_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        query_set = Task.objects.filter(owner=self.request.user.id)
        return query_set
