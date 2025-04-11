
from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='disease_images/')
    featured = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.name
