from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import MyUserCreationForm, MyUserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile


class ProfileCreateView(CreateView):
  form_class = MyUserCreationForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy("auth:login")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
  model = Profile
  form_class = MyUserUpdateForm
  template_name = 'registration/register.html'

  def get_queryset(self):
    qs = super(ProfileUpdateView, self).get_queryset()
    return qs.filter(owner=self.request.user)
  success_url = reverse_lazy("home:home")
