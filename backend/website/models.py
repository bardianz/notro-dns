from django.db import models

# Create your models here.

class HelpPage(models.Model):
    content = models.TextField()

    def __str__(self) -> str:
        return "STATIC body content for Help page"