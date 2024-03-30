from django.db import models

# Create your models here.

class HelpPage(models.Model):
    content = models.TextField()