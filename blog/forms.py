# first way insert data
from django import forms

# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
#

# second way insert data form
from django import forms
from .models import BlogPost
class BlogPostModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))
    class Meta:
        model = BlogPost
        fields = ['title', 'content']