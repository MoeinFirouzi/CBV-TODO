from django.urls import path
from account.views import LoginView, LogoutView

app_name = "account"

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
