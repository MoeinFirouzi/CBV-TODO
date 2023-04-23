from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import RedirectView
from account.forms import LoginForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import User


class LoginView(FormView):
    """
    This module contains a LoginView class that inherits from FormView.
    It handles user authentication and login.

    Attributes:
        form_class (LoginForm): A form class used for user login.
        template_name (str): A string representing the path to
        the HTML template used for rendering the login page.
        success_url (str): A string representing the URL to redirect
        to after successful login.

    Methods:
        form_invalid(self, form): Renders the login page with an
        error message if the submitted form is invalid.
        post(self, request, *args, **kwargs): Handles POST requests
        to authenticate and log in a user. If successful, redirects
        to success_url. If unsuccessful, renders the login page
        with an error message.
"""
    form_class = LoginForm
    template_name = "account/login.html"
    success_url = reverse_lazy("todo:index")

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        context = self.get_context_data(form=form)
        context["error"] = True
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
            else:
                # No backend authenticated the credentials
                return self.form_invalid(form)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(LoginRequiredMixin, RedirectView):
    """
     User Logout View
    """
    permanent = False
    pattern_name = "account:login"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class UserRegisterView(CreateView):
    """
    This module contains a class UserRegisterView which
    is a CreateView that handles user registration.

    Attributes:
        form_class (class): A class attribute that specifies
        the form to be used for user registration.

        success_url (str): A class attribute that specifies
        the URL to redirect to after successful user registration.

        template_name (str): A class attribute that specifies
        the name of the template to be used for rendering the
        user registration page.

    Methods:
        form_valid(self, form): Overrides the parent method to
        create a new User object with the cleaned data from the
        form and redirect to success_url if valid.

        get_context_data(self, **kwargs): Overrides the parent
        method to insert the form into the context dictionary.

        post(self, request, *args, **kwargs): Handles POST requests
        by instantiating a form instance with passed POST variables 
        and checking if it's valid. If valid, it creates a new 
        User object and redirects to success_url. Otherwise,
        it returns an invalid form.
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy("account:login")
    template_name = "account/UserRegister.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = User.objects.create_user(
            email=form.cleaned_data.get("email"),
            password=form.cleaned_data.get("password1"),
            first_name=form.cleaned_data.get("first_name"),
            last_name=form.cleaned_data.get("last_name")
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            if password1 == password2:
                email = form.cleaned_data.get("email")
                if not User.objects.filter(email=email).exists():
                    return self.form_valid(form)

            return self.form_invalid(form)

        else:
            return self.form_invalid(form)
