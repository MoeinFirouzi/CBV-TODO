from django.urls import path
from todo_app.views import IndexView

app_name = "todo"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
