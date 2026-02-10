
from rest_framework import serializers
from . import models

class ClientSerializer(serializers.ModelSerializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField(max_length=70)
   age = serializers.IntegerField(
      min_value=18, max_value=100
   )

   class Meta:
      model = models.Client
      fields = ['id', 'name', 'age', 'created_at']

class EmployeeSerializer(serializers.ModelSerializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField(max_length=70)
   registragion = serializers.CharField(max_length=50)

   class Meta:
      model = models.Employee
      fields = ['id', 'name', 'registragion', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
   id = serializers.IntegerField(read_only=True)
   description = serializers.CharField(max_length=100)
   quantity = serializers.DecimalField(max_digits=10, decimal_places=2)

   class Meta:
      model = models.Product
      fields = ['id', 'description', 'quantity', 'created_at']

class SaleSerializer(serializers.ModelSerializer):
   id = serializers.IntegerField(read_only=True)
   client = serializers.PrimaryKeyRelatedField(queryset=models.Client.objects.all())
   employee = serializers.PrimaryKeyRelatedField(queryset=models.Employee.objects.all())
   product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all())
   nrf = serializers.CharField(max_length=50)

   class Meta:
      model = models.Sale
      fields = ['id', 'client', 'employee', 'product', 'nrf', 'created_at']

