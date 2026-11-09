from django.db import models


class Innovation(models.Model):
    title = models.CharField(max_length=200)
    innovator_name = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    innovation_area = models.CharField(max_length=100)
    description = models.TextField()

    STATUS_CHOICES = [
        ('Idea', 'Idea'),
        ('Prototype', 'Prototype'),
        ('Developed', 'Developed'),
        ('Commercialized', 'Commercialized'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Idea'
    )

    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
