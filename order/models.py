from django.db import models
from account.models import Customer
from product.models import Product
from django.core.validators import MinLengthValidator
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Order(models.Model):

    name = models.CharField('name', max_length=50, blank=True, null=True)
    surname = models.CharField('surname', max_length=50, blank=True, null=True)
    email = models.EmailField('email',max_length=50, blank=True, null=True)
    tel_number = models.CharField('telefon', max_length=10, validators=[MinLengthValidator(10)], error_messages={'required': 'Mobil nomre 10 reqemli olmalidir'}, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField('Complete', default=False)
    transaction_id = models.CharField('Transaction id', max_length=100, null=True)
    message = models.TextField("Comment", null=False, blank=True)
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
    def get_discount_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_disco for item in orderitems])
        return total
        
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="order_items")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Quantity', default=0, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)

    
    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def get_total(self):
        total = self.product.get_price * self.quantity
        return total
    
    @property
    def get_disco(self):
        return self.product.get_discount * self.quantity

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Order items'
        verbose_name_plural = 'Order items'
        ordering = ('created_at',)
    
    def __str__(self):
        return self.product.title
    
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





# class Checkout(models.Model):
#     #information
#     NUMBER_CHOICES = (
#         ('050', '050'),
#         ('051', '051'),
#         ('055', '055'),
#         ('070', '070'),
#         ('077', '077'),
#         ('099', '099'),
#     )
#     order = models.OneToOneField(Order, on_delete=models.CASCADE, blank=True, null=True)
#     name = models.CharField('name', max_length=50)
#     surname = models.CharField('surname', max_length=50)
#     email = models.EmailField('email',max_length=50)
#     num_title = models.CharField('num title',max_length=10, choices=NUMBER_CHOICES)
#     tel_number = models.CharField('telefon', max_length=20)
#     # yuxaridakinin icinden cixdi validators=[MinLengthValidator(7)], error_messages={'required': 'Mobil nomre 7 reqemli olmalidir'}

#     # tel_number = PhoneNumberField()
#     message = models.TextField("Comment", null=True, blank=True)

#     # moderations
#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

#     class Meta:
#         db_table = ('checkout')
#         verbose_name = ('checkout')
#         verbose_name_plural = ('checkout')
        
#     def __str__(self):
#         return self.name