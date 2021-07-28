from django import forms
from django.forms.widgets import Textarea
class addStoryForm(forms.Form):
    title = forms.CharField(label='title',max_length=200)
    content = forms.CharField(label='content',widget=Textarea)
    image = forms.ImageField()