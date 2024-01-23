from django import forms
from book_management.models import *

class BookEntityForm(forms.ModelForm):
    class Meta:
        model = BookEntity
        fields = "__all__"

class AuthorEntityForm(forms.ModelForm):
    class Meta:
        model = AuthorEntity
        fields = "__all__"


