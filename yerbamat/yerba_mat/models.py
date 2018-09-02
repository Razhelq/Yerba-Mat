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
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    picture = models.ImageField(
        verbose_name='pictures',
        upload_to='pictures/',
        null=True,
    )
