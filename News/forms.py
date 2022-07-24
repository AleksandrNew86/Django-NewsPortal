from django import forms
from .models import Post


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'category_post', 'title_post', 'text_post']
        labels = {
            'category_post': "Категория",
            'author': 'Автор',
            'title_post': 'Название',
            'text_post': 'Текст'
        }
        empty_labels = {
            'text_post': Post.text_post
        }

