from django.db import models
from django.utils import timezone


class Email(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=70)
    e_mail = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name