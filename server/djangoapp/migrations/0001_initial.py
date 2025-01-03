# Generated by Django 5.1.4 on 2025-01-03 17:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('founded_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2025)])),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon'), ('TRUCK', 'Truck'), ('COUPE', 'Coupe'), ('HATCHBACK', 'Hatchback')], default='SUV', max_length=10)),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(2015)])),
                ('fuel_type', models.CharField(choices=[('GAS', 'Gasoline'), ('DIESEL', 'Diesel'), ('ELECTRIC', 'Electric'), ('HYBRID', 'Hybrid')], default='GAS', max_length=20)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.carmake')),
            ],
        ),
    ]
