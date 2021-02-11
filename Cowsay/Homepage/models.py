from django.db import models
from django.utils import timezone

class CowsayDisplay(models.Model):
    userInputText = models.CharField(max_length = 100)
    cowsayDisplay = models.CharField
    publishDate = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.userInputText