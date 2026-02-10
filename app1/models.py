from django.db import models

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )
    created_at =models.DateTimeField(
       db_column='dt_created',
       auto_now_add=True,
       null=True,
    )
    modified_at = models.DateTimeField(
    db_column='dt_modified',
    auto_now=True,
    null=True,
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    class Meta:
        abstract = True
        managed = True

class Product(ModelBase):
    description = models.TextField(
        db_column='description',
        null=False
    )
    quantity = models.IntegerField(
        db_column='quantity',
        null=False,
        default=0
    )

class Client(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=255,
        null=False
    )
    age = models.IntegerField(
        db_column='age',
        null=False
    )
    rg = models.CharField(
        db_column='rg',
        max_length=20,
        null=False,
        unique=True
    )
    cpf = models.CharField(
        db_column='cpf',
        max_length=20,
        null=False,
        unique=True
    )

class Employee(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=255,
        null=False
    )
    registragion = models.CharField(
        db_column='registration',
        max_length=50,
        null=False,
        unique=True
    ) 

    def __str__(self):
        return self.name, self.registragion

class Sale(ModelBase):
    product = models.ForeignKey(
        Product,
        db_column='product_id',
        null=False,
        on_delete=models.DO_NOTHING
    )
    client = models.ForeignKey(
        Client,
        db_column='client_id',
        null=False,
        on_delete=models.DO_NOTHING
    )
    employee = models.ForeignKey(
        Employee,
        db_column='employee_id',
        null=False,
        on_delete=models.DO_NOTHING
    )
    nrf = models.CharField(
        db_column='nrf',
        max_length=50,
        null=False,
        unique=True
    )