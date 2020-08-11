from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Genre Name')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20, verbose_name='Language Name')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Book Title')
    author = models.CharField(max_length=50, verbose_name='Book Author')
    publication = models.CharField(max_length=100, verbose_name='Book Publication')
    image = models.ImageField(verbose_name='Book Image', null=True, blank=True)
    description = models.TextField(max_length=1000, verbose_name='Book Description', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Book Price')
    contact_number = models.CharField(max_length=40, verbose_name='Contact Number')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Book Created_at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Book Updated_at')
    genre = models.ForeignKey(Genre, related_name='books', related_query_name='book', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='books', related_query_name='book', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='book', related_query_name='book', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
        # return reverse('book_edit', args=[str(self.id)])

    class Meta:
        ordering = ['-created_at']