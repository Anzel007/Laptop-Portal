from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    image = models.ImageField(upload_to='laptops/')

    def __str__(self):
        return self.name
