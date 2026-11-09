from django.db import models


class IPR(models.Model):
    IPR_TYPE_CHOICES = [
        ('Patent', 'Patent'),
        ('Copyright', 'Copyright'),
        ('Trademark', 'Trademark'),
    ]

    STATUS_CHOICES = [
        ('Filed', 'Filed'),
        ('Under Examination', 'Under Examination'),
        ('Granted', 'Granted'),
        ('Rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=200)
    applicant_name = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)

    ipr_type = models.CharField(
        max_length=20,
        choices=IPR_TYPE_CHOICES
    )

    description = models.TextField()

    application_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Filed'
    )

    filing_date = models.DateField()

    def __str__(self):
        return self.title
