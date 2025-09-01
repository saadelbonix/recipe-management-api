from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
from django.contrib.auth import login
from .forms import SignUpForm

class SignUpView(FormView):
    template_name = "users/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Welcome, your account has been created.")
        login(self.request, user)
        return super().form_valid(form)
