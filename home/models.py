from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorie(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Size(models.Model):
    name=models.CharField(max_length=5)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=120)
    price=models.IntegerField()
    description=models.TextField()
    img=models.ImageField(upload_to='product/')
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    price=models.IntegerField()
    description=models.TextField()
    img=models.ImageField(upload_to='product/')
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
