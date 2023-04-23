from django.urls import path
from account.views import LoginView, LogoutView, UserRegisterView,\
    UserUpdateView, UserDeleteView

app_name = "account"

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', UserRegisterView.as_view(), name="signup"),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name="user_update"),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name="user_delete"),
]
