from django.forms import ModelForm, RadioSelect, TextInput
from .models import SetUpModel


class SetUpModelForm(ModelForm):
  class Meta:
    model = SetUpModel
    fields = "__all__"
    exclude = ('owner',)
    widgets = {
      'result': RadioSelect,
      'Asset_Name': TextInput(attrs={'list': 'asset-list'}),
    }


class UpdateSetupForm(ModelForm):
  class Meta:
    model = SetUpModel
    fields = "__all__"
    exclude = ('owner',)
