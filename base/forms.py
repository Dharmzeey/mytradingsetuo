from django.forms import ModelForm, RadioSelect
from .models import SetUpModel


class SetUpModelForm(ModelForm):
  class Meta:
    model = SetUpModel
    fields = "__all__"
    widgets = {'result': RadioSelect}
