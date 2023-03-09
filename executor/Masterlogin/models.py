from django.db import models

# Create your models here.


class Calculation(models.Model):
    input_string = models.CharField(max_length=200)
    result = models.FloatField()

class CalculationLog(models.Model):
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)