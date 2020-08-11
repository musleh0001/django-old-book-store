from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication', 'description', 'price', 'contact_number', 'genre', 'language', 'image']