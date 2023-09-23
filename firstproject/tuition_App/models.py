from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    content = models.TextField()

    # model mathod
    def __str__(self):
        return self.name
