# Generated by Django 2.1.1 on 2018-09-05 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yerba_mat', '0003_remove_basket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='yerba_mat.Client'),
        ),
    ]
