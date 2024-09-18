from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    birthday = forms.DateTimeField(label='Дата рождения')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'birthday',
            'email',
            'password1',
            'password2',
        )

# Create your models here.
