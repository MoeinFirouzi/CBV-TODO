from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from account.forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(FormView):
    """
    User Login View
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
                login(self.request, user)
            else:
                # No backend authenticated the credentials
                return self.form_invalid(form)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False
    pattern_name = "account:login"

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return super().get(request, *args, **kwargs)
    
