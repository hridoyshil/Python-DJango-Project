from django.db import models
from django.utils.timezone import now

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    content = models.TextField()

    # model mathod
    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY = (
        ("Teacher", "Teacher"),
        ("Student", "Student"),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField()
    salay = models.FloatField()
    details = models.TextField()
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
