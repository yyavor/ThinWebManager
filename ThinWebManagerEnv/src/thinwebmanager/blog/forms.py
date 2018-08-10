from django import forms
from .models import Article
from datetime import datetime


class ArticleForm(forms.ModelForm):
    date = forms.DateTimeField(initial=datetime.now(), required=False)

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "date"
        ]
