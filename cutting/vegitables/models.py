from django.db import models

# Create your models here.

class vegitables(models.Model):

    name = models.CharField(max_length=10)
    price = models.IntegerField()
    image = models.TextField(max_length=100, null=True, blank=True) #image url
    
    def __str__(self):
        return self.name
    
class customer(models.Model):

     name = models.ForeignKey(vegitables,on_delete=models.CASCADE)
     quantity = models.FloatField(null=True, blank=True)
     cust = models.CharField(max_length=100, null=True, blank=True)  
     address = models.TextField()
     phone = models.IntegerField()

    # vegitables = models.ForeignKey(vegitables,on_delete=models.CASCADE)
     def total_amount(self):
        return self.quantity * self.name.price

