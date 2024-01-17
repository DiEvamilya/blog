
from django import forms
from post.models import Category

class CreateCategoryModelForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',  )