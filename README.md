# Ex02 Django ORM Web Application
## Date:13-10-2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```

admin.py
from django.contrib import admin
from.models import Blinkit,BlinkitAdmin
admin.site.register(Blinkit,BlinkitAdmin)


models.py
from django.db import models
from django.contrib import admin
class Blinkit(models.Model):
    Delivery_No =models.IntegerField(primary_key=True)
    Customer_Name=models.CharField(max_length=20)
    Product_Name=models.CharField(max_length=20)
    Price=models.FloatField()
    Product_Quantity=models.IntegerField()
    Tax=models.IntegerField()
    Total_Amount=models.FloatField()
    Phone_No=models.IntegerField()
    Customer_Address=models.TextField()

class BlinkitAdmin(admin.ModelAdmin):
    list_display=["Delivery_No","Customer_Name","Product_Name","Price","Product_Quantity","Tax","Total_Amount","Phone_No","Customer_Address"]
 
```



## OUTPUT
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/7655f139-73aa-48d3-8b92-8de8e0303f2f" />




## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
