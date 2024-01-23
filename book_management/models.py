from django.db import models

# Create your models here.

class AuthorEntity(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class BookEntity(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(AuthorEntity,on_delete = models.CASCADE)
    publication_year = models.PositiveIntegerField()
    isbn = models.PositiveIntegerField()
    

    def __str__(self):
        return self.title


