from django import template
from datetime import datetime
from django.db import models
from django.utils import timezone
from amdtelecom.utils import unique_slug_generator
from django_resized import ResizedImageField
from colorfield.fields import ColorField
from django.db.models.signals import pre_save

from account.models import Customer
from .common import slugify

register = template.Library()




class Tag(models.Model):

    title = models.CharField('Title', max_length=100, db_index=True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tag'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title


class Marka(models.Model):  
    # informations
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField('Image', blank=True, upload_to='marka_images')
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)
    

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'marka'
        verbose_name = 'Marka'
        verbose_name_plural = 'Markas'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):        
        title = Marka.objects.filter(title=self.title).first()
        super(Marka, self).save(*args, **kwargs)
        self.slug = f'{slugify(self.title)}-{self.id}'
        super(Marka, self).save(*args, **kwargs)


class Category(models.Model):
    # relation
    parent = models.ManyToManyField('self', related_name='children', blank=True)

    # information
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField('Image', blank=True, upload_to='categories_images')
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)
    is_main = models.BooleanField('is_main', default=False)
    is_second = models.BooleanField('is_second', default=False)
    is_third = models.BooleanField('is_third', default=False)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('created_at', 'title')
        unique_together = ('slug',)

    def __str__(self):
        if self.is_main:
            title = f'{self.title}'
        elif self.is_second:
            title = f'{self.title}'
        else:
            title = f'{self.parent.all().last()} {self.title} '
        return title 

    def save(self, *args, **kwargs):        
        super(Category, self).save(*args, **kwargs)
        print(self.parent.all().last())
        if self.parent.all().last():
            parent = str(self.parent.all().last())
            self.slug = f'{slugify(parent)}-{slugify(self.title)}'
        else:
            self.slug = f'{slugify(self.title)}'    
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    """
    very important table
    """
    # relations
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    same_product = models.ManyToManyField('self', related_name='same_products', blank=True)
    category = models.ManyToManyField('Category', related_name='categories')
    who_like = models.ManyToManyField(Customer, related_name='liked_products', blank=True)
    marka = models.ManyToManyField(Marka, related_name='marka', blank=True)


    # informations
    color_title = models.CharField('Color Name', max_length=50, blank=True, null=True)
    color_code = ColorField('Color code', default='', blank=True, null=True)
    title = models.CharField('Title', max_length=100, db_index=True)
    slug = models.SlugField('Slug', editable=False, max_length=110, unique = True, blank=True)
    sku = models.CharField('SKU', max_length=50, db_index=True)
    description = models.TextField('Description', null=True, blank=True)
    sale_count = models.IntegerField('Sale Count', default=0)
    is_published = models.BooleanField("Publishe", default=True)
    is_new = models.BooleanField('is_new', default=True)
    is_featured = models.BooleanField('is_featured', default=False)
    is_discount = models.BooleanField('is_discount', default=False)

    # price info
    CHOICES = (
        (1, 'Not'),
        (2, 'Percent'),
        (3, 'Unit'),
    )
    price = models.DecimalField('Price', max_digits=7, decimal_places=2)
    discount_type = models.PositiveIntegerField("Discount Type", choices=CHOICES, default=1)
    discount_value = models.IntegerField('Discount Value', null=True, blank=True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('title', 'slug')
        # slug unique
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at', 'title')


    def save(self, *args, **kwargs):        
        super(Product, self).save(*args, **kwargs)
        self.slug = f'{slugify(self.title)}-{self.id}'
        super(Product, self).save(*args, **kwargs)


    def get_price(self):
        if self.discount_type == 1:
            return self.price
        elif self.discount_type == 2:
            return self.price - (self.price * self.discount_value / 100)
        else:
            return self.price - self.discount_value
    
    def get_is_discount(self):
        if self.get_price() < self.price:
            is_discount = True
    
    def get_is_new(self):
        delta = datetime.now().date() - self.created_at
        if delta.days <= 30:
            is_new = True

    def __str__(self):
        return f'{self.title} {self.color_title}'


class Product_details(models.Model):
    # relations
    product = models.ForeignKey('product.Product', related_name='products', default="Not", on_delete=models.CASCADE, blank=True, null=True)
    product_details_property_name = models.ForeignKey("Product_details_property_name", on_delete=models.CASCADE, related_name='product_details_property_name')
    product_details_propert_value = models.ForeignKey("Product_details_property_value", on_delete=models.CASCADE, related_name='product_details_property_value')
    is_feature = models.BooleanField("Is feature", default=False, blank=True, null=True)
    is_detail = models.BooleanField("Is detail", default=False, blank=True, null=True)
    is_file = models.BooleanField('Is file', default=False, blank=True, null=True)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    class Meta:
        db_table = 'Product details'
        verbose_name = 'Product details'
        verbose_name_plural = 'Products details'


class Product_details_property_name(models.Model):
    # informations 
    title = models.CharField("Title", max_length=50, blank=True, null=True)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Property name '
        verbose_name = 'Property name'
        verbose_name_plural = 'Properties names'


class Product_details_property_value(models.Model):
    # relations 

    # informations 
    content = models.CharField("Content", max_length=50, blank=True, null=True)
    file = models.FileField("File", upload_to='products_files', max_length=100, blank=True, null=True)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content

    class Meta:
        db_table = 'Property value'
        verbose_name = 'Property value'
        verbose_name_plural = 'Properties values'


class Product_images(models.Model):
    # product-un butun sekilleri burda saxlanacaq
    # is_main true olan esas shekildi
    # is_second_main olan shekil coxlu product sehifesinde hover edende gelen sekildi

    # relations
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    # informations
    # image = models.ImageField('Image', upload_to='product_images')
    image = ResizedImageField(size=[800, 500], upload_to='product_images')
    is_main = models.BooleanField('Main Image', default=False) 
    is_second_main = models.BooleanField('Second Main Image', default=False) 

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'image'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.image}'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Product_colors(models.Model):
    # eyni bir product bir nece renge sahib ola bildiyi ucun yaratdim    
    # relations
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')

    # informations
    coler_title = models.CharField('Title', max_length=50, db_index=True, blank=True, null=True)
    color_code = models.CharField('Title', max_length=50, db_index=True, blank=True, null=True)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Product colors'
        verbose_name = 'Product color'
        verbose_name_plural = 'Product colors'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'


