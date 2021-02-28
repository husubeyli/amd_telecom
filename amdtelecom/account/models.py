from django.db import models

# Create your models here.

class Customer(models.Model):
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'name: {self.device}'
