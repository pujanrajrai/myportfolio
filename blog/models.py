from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(
        upload_to="blogs/"
    )
    created_date = models.DateField(
        auto_now=True
    )
    name = models.CharField(
        max_length=100
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    description = models.TextField()

    def __str__(self):
        return self.name
