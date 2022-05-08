from django.db.models import Q
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
      recent_setups = SetUpModel.objects.all().filter(owner=request.user).order_by('-date')[(total_setups - 10): total_setups]
    else:
      recent_setups = SetUpModel.objects.all().filter(owner=request.user).order_by('-date')
    context = {
      'recent_setups': recent_setups
    }

    # THIS FUNCTION BELOW HANDLES THE SEARCH
    q = request.GET.get('q', '')

    # THIS CHECKS IF THE Q HAS A STR
    if q == '':
      return render(request, self.template_name, context)

    search_result = SetUpModel.objects.filter(owner=request.user).filter(
      Q(Asset_Name__icontains=q)
    ).order_by('-date')
    context.update({
      'search_result': search_result
    })
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
  # success_url = reverse_lazy("home:detail")

  def get_queryset(self):
    qs = super(UpdateSetup, self).get_queryset()
    return qs.filter(owner=self.request.user)

  def get_success_url(self):
    pk = self.kwargs['pk']
    return reverse_lazy('home:detail', kwargs={'pk': pk})


class SetupDetail(LoginRequiredMixin, View):
  template_name = "base/setup_detail.html"

  def get(self, request, pk):
    setup_detail = SetUpModel.objects.get(id=pk)
    context = {
      'setup_detail': setup_detail
    }
    return render(request, self.template_name, context)

