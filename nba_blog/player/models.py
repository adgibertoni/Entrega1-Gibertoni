from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    number = models.IntegerField()
    points = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.last_name} | Country: {self.country}"
    