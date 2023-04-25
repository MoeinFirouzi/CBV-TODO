from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from todo_app.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy


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
        query_set = Task.objects.filter(
            owner=self.request.user.id).order_by("-id")
        return query_set


class TaskDetailView(DetailView):
    """
    This class displays a detailed view of a single Task instance.

    Attributes:
        model (Task): The model that this DetailView is associated with.
    """
    model = Task


class TaskCreateView(CreateView):
    """
    This module contains a class TaskCreateView that inherits from CreateView.

    Attributes:
    model (Task): A model representing the task.
        fields (list): A list of fields to be displayed in the form.
        template_name (str): The name of the HTML template to be used for
        rendering the view.
        success_url (str): The URL to redirect to after a successful
        form submission.

    Methods:
        form_valid(self, form): Overrides the default implementation of
        form_valid method. If the form is valid, it saves the associated
        model and sets its owner as the current user.
        Then it redirects to success_url.

    """
    model = Task
    fields = ["title", "description"]
    template_name = 'todo_app/task_create.html'
    success_url = reverse_lazy("todo:tasks")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class TaskDeleteView(DeleteView):
    """
    this class-based view allows users to delete a specific Task object.
    Upon successful deletion, the user is redirected to the main tasks list page.

    Attributes:
        model (Task): The Task model to be deleted.
        success_url (str): The URL to redirect to upon successful deletion,
                      using reverse_lazy to resolve the "todo:tasks" URL pattern.
    """
    model = Task
    success_url = reverse_lazy("todo:tasks")
