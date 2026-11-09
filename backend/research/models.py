from django.db import models




class ResearchProject(models.Model):
    title = models.CharField(max_length=200)
    researcher_name = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    research_area = models.CharField(max_length=100)
    description = models.TextField()
    
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Planned'
    )

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
