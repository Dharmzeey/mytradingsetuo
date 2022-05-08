from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import MyUserCreationModel


class MyUserCreationForm(UserCreationForm):
  class Meta:
    model = MyUserCreationModel
    fields = ['username', 'email', 'password1', 'password2']


class MyUserUpdateForm(ModelForm):
  class Meta:
    model = MyUserCreationModel
    fields = ['avatar', 'name', 'username', 'email', 'bio']
