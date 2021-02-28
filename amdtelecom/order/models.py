from django.db import models
from account.models import Customer
from product.models import Product
from django.core.validators import MinLengthValidator
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField('Complete', default=False)
    transaction_id = models.CharField('Transaction id', max_length=100, null=True)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order'  
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
        
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    
    def __str__(self):
        return f'{self.id}'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Quantity', default=0, null=True, blank=True)
    
    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def get_total(self):
        total = self.product.get_price() * self.quantity
        return total

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Order items'
        verbose_name_plural = 'Order items'
        ordering = ('created_at',)
    
    def __str__(self):
        return f'Quantity {self.quantity}'
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField('Adress', max_length=200, null=False)
    city = models.CharField('City', max_length=200, null=False)
    state = models.CharField('State', max_length=200, null=False)
    zipcode = models.CharField('Zipcode', max_length=200, null=False)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shipping_address'
        verbose_name = 'Shipping address'
        verbose_name_plural = 'Shipping addresses'
        ordering = ('created_at',)

    def __str__(self):
        return self.address


from django.db import models
from django.utils.translation import gettext as _


class Checkout(models.Model):
    #information
    NUMBER_CHOICES = (
        ('050', '050'),
        ('051', '051'),
        ('055', '055'),
        ('070', '070'),
        ('077', '077'),
        ('099', '099'),
    )

    name = models.CharField('name', max_length=50)
    surname = models.CharField('surname', max_length=50)
    email = models.EmailField('email',max_length=50)
    num_title = models.CharField('num title',max_length=10, choices=NUMBER_CHOICES)
    tel_number = models.CharField('telefon', max_length=7, validators=[MinLengthValidator(7)], error_messages={'required': 'Mobil nomre 7 reqemli olmalidir'})

    # moderations
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = ('checkout')
        verbose_name = ('checkout')
        verbose_name_plural = ('checkout')
        
    def __str__(self):
        return self.name