from django.db import models
class Crop(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    price_per_kg=models.IntegerField()
    description=models.TextField()
    def __str__(self):
        return self.name

# Create your models here.
