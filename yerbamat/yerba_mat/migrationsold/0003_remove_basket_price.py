# Generated by Django 2.1.1 on 2018-09-05 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yerba_mat', '0002_auto_20180905_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='price',
        ),
    ]