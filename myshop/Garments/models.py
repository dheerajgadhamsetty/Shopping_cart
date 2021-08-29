from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class Formalshirt(models.Model):
    name = models.CharField(max_length=100)
    photo = models.FileField(blank=True)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self): 
        return self.name

class Trousers(models.Model):
    name = models.CharField(max_length=100)
    photo = models.FileField(blank=True)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self): 
        return self.name
        
class Orders(models.Model):
    formalshirt = models.ForeignKey(Formalshirt, on_delete=CASCADE, default=True)
    trousers = models.ForeignKey(Trousers, on_delete=CASCADE, default=True)



    
