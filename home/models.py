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
