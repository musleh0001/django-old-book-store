from django.contrib import admin
from .models import Genre, Language, Book

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book)