from django.urls import path
from account.views import LoginView, LogoutView, UserRegisterView

app_name = "account"

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', UserRegisterView.as_view(), name="signup"),
]
