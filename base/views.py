from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import SetUpModel
from .forms import SetUpModelForm, UpdateSetupForm


class BaseView(LoginRequiredMixin, View):
  template_name = "base/home.html"

  def get(self, request):
    # GET THE NUMBER OF SETUPS AND DISPLAY THE LAST 10 AS RECENT SETUP
    total_setups = SetUpModel.objects.all().filter(owner=request.user).count()
    if total_setups >= 10:
      recent_setups = SetUpModel.objects.all().filter(owner=request.user)[(total_setups - 10): total_setups]
    else:
      recent_setups = SetUpModel.objects.all().filter(owner=request.user)
    context = {
      'recent_setups': recent_setups
    }
    return render(request, self.template_name, context)


class CreateSetUp(LoginRequiredMixin, CreateView):
  form_class = SetUpModelForm
  template_name = 'base/setupmodel_form.html'
  success_url = reverse_lazy("home:home")

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super(CreateSetUp, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    setup_model = SetUpModel.objects.all().filter(owner=self.request.user)
    context['setup_model'] = setup_model
    return context


class UpdateSetup(LoginRequiredMixin, UpdateView):
  model = SetUpModel
  form_class = UpdateSetupForm
  template_name = 'base/setupmodel_form.html'
  success_url = reverse_lazy("home:home")


class SetupDetail(LoginRequiredMixin, View):
  template_name = "base/setup_detail.html"

  def get(self, request, pk):
    setup_detail = SetUpModel.objects.get(id=pk)
    context = {
      'setup_detail': setup_detail
    }
    return render(request, self.template_name, context)

