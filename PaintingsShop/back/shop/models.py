from django.db import models

# Create your models here.

# Таблиця Picture

class Picture(models.Model):
    image = models.ImageField(upload_to='pictures/')
    description = models.TextField()

    def __str__(self):
        return self.description[:30]
    
    class Meta:
        ordering = ["id"]

# Таблиця About

class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["id"]