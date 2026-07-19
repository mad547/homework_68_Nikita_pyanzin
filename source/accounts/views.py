from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('articles:list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)