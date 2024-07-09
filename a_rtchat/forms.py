from django.forms import ModelForm
from django import forms
from .models import GroupMessage

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Enter Message...', 'class': 'p-4 text-black','maxlength':'300','autofocus':'True'}),
        }