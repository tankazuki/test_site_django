from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField

from app01.models import Memo


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('title', 'memo',)


class SignUpForm(UserCreationForm):
    email = EmailField(label='メールアドレス', required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

