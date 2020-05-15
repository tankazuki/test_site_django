from django import forms

from app01.models import Memo, Like


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('title', 'memo',)

