from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    owner = models.CharField(max_length=40)
    found_in = models.DateField()

    def __str__(self):
        return f"{self.city} {self.name}"
    