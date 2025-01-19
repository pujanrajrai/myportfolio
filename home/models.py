from django.db import models
# Create your models here.


class Education(models.Model):
    title = models.CharField(
        max_length=100
    )
    starting_date = models.DateField()
    ending_date = models.DateField(
        null=True,
        blank=True
    )
    institution_name = models.CharField(
        max_length=100
    )
    description = models.TextField()

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(
        max_length=100
    )
    email = models.EmailField(
        max_length=255
    )
    subjects = models.CharField(
        max_length=100
    )
    message = models.TextField()

    def __str__(self):
        return self.name
