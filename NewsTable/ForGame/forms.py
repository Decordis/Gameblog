from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'description',
            'author',
            'category',
        ]

        def clean(self):
            cleaned_data = super().clean()
            description = cleaned_data.het('description')
            if description is not None and len(description) < 20:
                raise ValidationError({
                    'description': 'Слишком маленькое!'
                })
            name = cleaned_data.get('name')
            if name == description:
                raise ValidationError('Описание не должно быть идентичным названию')

            author = cleaned_data.get('author')
            if author is None:
                raise ValidationError('Поле автора не должно быть пустым')

            return cleaned_data


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'comment_text',
        ]

