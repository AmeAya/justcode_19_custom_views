from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.surname} {self.name}"


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    year = models.IntegerField()
    is_popular = models.BooleanField(default=False)
    # default -> Стандартное значение

    from django.contrib.auth.models import User
    users = models.ManyToManyField(User, blank=True)
    # Привязываем к django Users через Many-to-Many

    def __str__(self):
        return self.name
