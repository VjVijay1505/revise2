from django.db import models
import uuid

# Create your models here.
class Site(models.Model):
    VALUE_TYPE = (
        ('Petrol', 'Petrol station'),
        ('Diesel', 'Diesel station'),
        ('Gas', 'Gas station'),
        ('Electric', 'Electric station')
    )
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=VALUE_TYPE)
    address = models.TextField(blank=True, null=True)
    files = models.ManyToManyField('Upload')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self) -> str:
        return self.name

class Upload(models.Model):
    myFile = models.FileField(blank=True, null=True)
    sites = models.ForeignKey(Site, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self) -> str:
        return str(self.id)

