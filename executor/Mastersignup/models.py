from django.db import models

# Create your models here.



class Result(models.Model):
    expression = models.CharField(max_length=100)
    result = models.FloatField()

    def __str__(self):
        return f"{self.expression} = {self.result}"
