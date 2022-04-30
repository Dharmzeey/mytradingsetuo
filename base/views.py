from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import SetUpModel
from .forms import SetUpModelForm


class BaseView(LoginRequiredMixin, View):
  template_name = "base/home.html"

  def get(self, request):
    return render(request, self.template_name)


class CreateSetUp(LoginRequiredMixin, CreateView):
  form_class = SetUpModelForm
  template_name = 'base/setupmodel_form.html'
  success_url = reverse_lazy("home:home")

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    setup_model = SetUpModel.objects.all()
    context['setup_model'] = setup_model
    return context
