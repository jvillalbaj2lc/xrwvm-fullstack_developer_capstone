from django.contrib import admin
from .models import CarMake, CarModel


# Customizing CarMake admin
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'country', 'founded_year')  # Display these fields in the list view
    search_fields = ('name', 'country')  # Add a search box for these fields


# Customizing CarModel admin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id', 'fuel_type')  # Fields to display in list view
    list_filter = ('type', 'fuel_type', 'car_make')  # Add filters for these fields
    search_fields = ('name', 'car_make__name')  # Add search functionality for car model name and car make name


# Registering models with their custom admin configurations
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
