from django.db import models

# Create your models here.

class Property(models.Model):
    
    address = models.CharField(max_length=100)
    
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    property_type = models.CharField(max_length=100)
    
    number_of_bedrooms = models.PositiveIntegerField()
    
    square_footage = models.PositiveIntegerField()
    
    location = models.CharField(max_length=200)
    
    property_image = models.ImageField(upload_to="property_images",null=True,blank=True)
    
    def __str__(self):
        
        return self.address
       
       
    
    
    
    
