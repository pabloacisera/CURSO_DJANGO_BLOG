from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'pub_date', 'author']
