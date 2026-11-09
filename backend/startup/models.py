from django.db import models


class Startup(models.Model):
    STAGE_CHOICES = [
        ('Idea', 'Idea'),
        ('Early Stage', 'Early Stage'),
        ('Growth Stage', 'Growth Stage'),
        ('Established', 'Established'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Closed', 'Closed'),
    ]

    name = models.CharField(max_length=200)
    founder_name = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    sector = models.CharField(max_length=100)
    description = models.TextField()

    stage = models.CharField(
        max_length=30,
        choices=STAGE_CHOICES,
        default='Idea'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    founded_date = models.DateField()

    def __str__(self):
        return self.name
