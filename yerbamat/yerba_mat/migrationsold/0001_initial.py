# Generated by Django 2.1.1 on 2018-09-05 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('phone', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('amount', models.IntegerField(default=0)),
                ('rate', models.FloatField(default=0)),
                ('picture', models.ImageField(null=True, upload_to='pictures/', verbose_name='pictures')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='yerba_mat.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yerba_mat.Client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yerba_mat.Product')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yerba_mat.Client'),
        ),
        migrations.AddField(
            model_name='basket',
            name='product',
            field=models.ManyToManyField(to='yerba_mat.Product'),
        ),
    ]