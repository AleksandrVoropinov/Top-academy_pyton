from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Название статьи'}),
            'anons': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Анонс статьи'}),
            'date': DateTimeInput(attrs={'class': 'form-control',
                                         'placeholder': 'Дата публикации',
                                         'type': 'datetime-local'}),
            'full_text': TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Текст статьи'})
        }
