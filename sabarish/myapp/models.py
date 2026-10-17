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
