from django.db import models

# Create your models here.
class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.TextField() # Store as comma-separated

    def __str__(self):
        return self.author