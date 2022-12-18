from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['image','title', 'pub_date', 'content'] #we removed author
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }