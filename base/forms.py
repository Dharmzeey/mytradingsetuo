from django.forms import ModelForm, RadioSelect, TextInput, Textarea, FileInput
from .models import SetUpModel


class SetUpModelForm(ModelForm):
  class Meta:
    model = SetUpModel
    fields = ["schema", "Asset_Name", "Image_before", "Image_before2", "bias"]
    widgets = {
      'result': RadioSelect,
      'Asset_Name': TextInput(attrs={'list': 'asset-list'}),
      'bias': Textarea(attrs={'rows': '5'}),
      'Reason_For_be': Textarea(attrs={'rows': '5'})
    }


class UpdateSetupForm(ModelForm):
  class Meta:
    model = SetUpModel
    fields = "__all__"
    exclude = ('owner',)

    widgets = {
      'result': RadioSelect,
      'Asset_Name': TextInput(attrs={'list': 'asset-list', 'readonly': 'readonly'}),
      'bias': Textarea(attrs={'rows': '5'}),
      'Reason_For_be': Textarea(attrs={'rows': '5'}),
      'schema': TextInput(attrs={'readonly': 'readonly'}),
      # 'Image_before': FileInput(attrs={'readonly': 'readonly'}),
      # 'Image_before2': FileInput(attrs={'readonly': 'readonly'})
    }