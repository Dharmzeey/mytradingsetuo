from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import MyUserCreationForm, MyUserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import MyUserCreationModel


class MyUserCreationView(CreateView):
  form_class = MyUserCreationForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy("auth:login")


class MyUserUpdateView(LoginRequiredMixin, UpdateView):
  model = MyUserCreationModel
  form_class = MyUserUpdateForm
  template_name = 'registration/register.html'

  def get_queryset(self):
    qs = super(MyUserUpdateView, self).get_queryset()
    print(self.request.user)
    return qs.filter(username=self.request.user)
  success_url = reverse_lazy("home:home")
