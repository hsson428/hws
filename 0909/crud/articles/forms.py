from django import forms
from django.db import models
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = '__all__'