from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


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
    name = models.CharField(max_length=128, blank=True)
    lastname = models.CharField(max_length=128, blank=True)
    street = models.CharField(max_length=128, blank=True)
    post = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Basket(models.Model):
    person = models.OneToOneField(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through="InsideBasket")
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.person.name


class InsideBasket(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    items = models.IntegerField(default=0)

    def __str__(self):
        return self.basket.person.name


class Review(models.Model):
    person = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person.name


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    person = models.ForeignKey(Client, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    name = models.CharField(max_length=128, blank=True)
    lastname = models.CharField(max_length=128, blank=True)
    street = models.CharField(max_length=128, blank=True)
    post = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.person.name
