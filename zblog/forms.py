from django import forms

from .models import Zpost

class PostForm(forms.ModelForm):

    class Meta:
        model = Zpost
        fields = ('title', 'text',)
