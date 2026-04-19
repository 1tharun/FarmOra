from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    telugu_name = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=500, blank=True)  # URL or path
    farmer_id = models.IntegerField()

    def __str__(self):
        return self.name
