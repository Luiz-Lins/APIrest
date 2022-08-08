from django.db import models


class Author(models.model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.model):
    name = models.CharField(max_length=128)
    edition = models.PositiveIntegerField()
    publication_year = models.CharField(max_length=4)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.name
