from django import forms
from .models import Comment, Category, Thread


# class 

class CommentForm(forms.ModelForm): # with Meta we're overriding the Comment model
    class Meta:
        model = Comment
        fields = ("comment", )


choices = Category.objects.all().values_list("name", "name")
choice_list = [item for item in choices]


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ("title", "category", "body", "thread_image", )
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "category": forms.Select(choices=choice_list, attrs={"class":"form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }