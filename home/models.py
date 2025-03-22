from django.db import models

class WomenInTech(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='women/')

    def __str__(self):
        return self.name