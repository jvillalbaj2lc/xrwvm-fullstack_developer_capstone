# Uncomment the following imports before adding the Model code
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# CarMake Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make
    country = models.CharField(max_length=100, blank=True, null=True)  # Optional: Country of origin
    founded_year = models.IntegerField(
        validators=[
            MinValueValidator(1800),  # Assume car companies started around the 1800s
            MaxValueValidator(now().year)
        ],
        blank=True,
        null=True
    )  # Optional: Year the company was founded

    def __str__(self):
        return f"{self.name} ({self.description})"  # String representation


# CarModel Model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    dealer_id = models.IntegerField(blank=True, null=True)  # Make dealer_id optional
    name = models.CharField(max_length=100)  # Name of the car model
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
    ]  # Choices for car type
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Car type with limited choices
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),  # Ensure the year is within the range specified in the data
            MinValueValidator(2015)
        ]
    )  # Year field with validation
    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ('GAS', 'Gasoline'),
            ('DIESEL', 'Diesel'),
            ('ELECTRIC', 'Electric'),
            ('HYBRID', 'Hybrid'),
        ],
        default='GAS'
    )  # Optional: Type of fuel the car uses

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.type}, {self.year})"  # String representation
