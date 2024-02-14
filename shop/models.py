from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=55)
    pic=models.FileField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=75)
    detail=models.TextField()
    brand=models.CharField(max_length=55)
    country=models.CharField(max_length=55)
    guarantee=models.CharField(max_length=55)
    available=models.BooleanField()
    amount=models.PositiveIntegerField
    discount=models.PositiveSmallIntegerField(default=0)
    delivery=models.BooleanField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Picture(models.Model):
    picture=models.FileField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)


