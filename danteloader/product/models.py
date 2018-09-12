from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, max_length=10)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(unique=True, max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
