from django import forms
from django.core.exceptions import ValidationError

from .models import BlogPost, Tag


# class TagsAsString(forms.Field):
#     def to_python(self, value):
#         """Normalize data to a list"""
#         # Return an empty list if no input was given
#         if not value:
#             return []
#         return value.split(",")

#     def validate(self, value):
#         """Check or create tags"""
#         super().validate(value)
#         for tag in value:
#             Tag.objects.get_or_create(tag)


# class ModelCommaSeparatedChoiceField(forms.ModelMultipleChoiceField):
#     widget = forms.Textarea
#     def clean(self, value):
#         if value is not None:
#             value = [item.strip() for item in value.split(",")] # remove padding
#         return super(ModelCommaSeparatedChoiceField, self).clean(value)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost

        fields = ['title', 'body', 'tag']
        labels = {'title': 'Title', 'body': 'Body', 'tag': 'Tags'}
        widgets = {'body': forms.Textarea(attrs={'cols': 100})}
        # widgets = {'body': forms.Textarea(attrs={'cols': 100}), 'tag': forms.Textarea(attrs={'rows': 1})}


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {'name': 'Tag Name'}
        widgets = {'name': forms.Textarea(attrs={'cols': 20, 'rows': 1})}
