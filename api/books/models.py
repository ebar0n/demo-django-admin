from django.db import models
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.ForeignKey('locations.City', on_delete=models.CASCADE)
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Author(models.Model):
    artistic_name = models.CharField(max_length=30)
    user = models.ForeignKey(
        'auth.User', on_delete=models.SET_NULL,
        blank=True, null=True, limit_choices_to={'is_staff': False}
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Book(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def is_new(self):
        return self.publication_date.year == timezone.now().date().year


class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField(help_text='Quantity of books purchased')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        unique_together = (('book', 'user'),)
        ordering = ['-created_at']
        verbose_name = 'Book sale'
        verbose_name_plural = 'Book sales'


class BookSold(Sale):
    class Meta:
        proxy = True
        ordering = ['book__title']
        verbose_name = 'Book sold'
        verbose_name_plural = 'Books sold'
