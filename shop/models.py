from django.db import models

class manfacturer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    manfacturer = models.ForeignKey(manfacturer, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=100,
        choices=[
            ('Dairy', 'Dairy'),
            ('Grains', 'Grains'),
            ('Fruits', 'Fruits'),
            ('Vegetables', 'Vegetables'),
            ('Other', 'Other'),
        ]
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image=models.ImageField(upload_to='media/product_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class hardware(models.Model):
    weight = models.DecimalField(max_digits=10, decimal_places=2)
   

    