from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    amount = models.IntegerField(default=0)
    rate = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    picture = models.ImageField(
        verbose_name='pictures',
        upload_to='pictures/',
        null=True,
    )


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    phone = models.IntegerField(default=0)


class Basket(models.Model):
    person = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    items = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)


class Review(models.Model):
    person = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    creation_date = models.DateTimeField(auto_now=True)
