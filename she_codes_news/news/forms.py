from django import forms
from django.forms import ModelForm
from .models import NewsStory, Category


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'category','image','content'] #we removed author
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-field-test'}),      #added title line to try connect CSS
            'pub_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
            'category': forms.Select(attrs={'class': 'form-field-test'}),
            'image': forms.URLInput(attrs={'class': 'form-field-test'}),
            'content': forms.Textarea(attrs={'class': 'form-field-test', 'rows': 10}),
        }