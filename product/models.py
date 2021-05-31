from datetime import datetime, timedelta
from django.utils import timezone
from django import template
from django.db import models
from django_resized import ResizedImageField
from colorfield.fields import ColorField

from account.models import Customer
from .common import slugify

register = template.Library()



def one_month_from_today():
    return timezone.now() + timedelta(days=30)


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
    title = models.CharField('Başlıq', max_length=100, db_index=True)
    image = models.ImageField('Şəkil', blank=True, upload_to='marka_images')
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)
    

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'marka'
        verbose_name = 'Marka'
        verbose_name_plural = 'Markalar'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):  
        
        title = Marka.objects.filter(title=self.title).first()
        super(Marka, self).save(*args, **kwargs)
        if len(self.slug) == 0: 
            self.slug = f'{slugify(self.title)}-{self.id}'
        super(Marka, self).save(*args, **kwargs)


class Category(models.Model):
    # relation
    parent = models.ManyToManyField('self', related_name='children', blank=True)

    # information
    title = models.CharField('Başlıq', max_length=100, db_index=True)
    image = models.ImageField('Şəkil', blank=True, upload_to='categories_images')
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField('Slug', max_length=110, editable=False, default='', unique = True)
    is_main = models.BooleanField('Əsas', default=False)
    is_second = models.BooleanField('İkinci', default=False)
    is_third = models.BooleanField('Üçüncü', default=False)

    # moderations
    status = models.BooleanField('Aktiv', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'
        ordering = ('created_at', 'title')
        unique_together = ('slug',)
    

    @property
    def get_slug(self):
        slug = ''
        for item in self.parent.all():
            slug += item.title
        return slug


    def __str__(self):
        if self.is_main:
            title = f'{self.title}'
        elif self.is_second:
            title = f'{self.title}'
        else:
            title = f'{self.parent.all().last()} {self.title} '
        return title



class Product(models.Model):
    """
    very important table
    """
    # relations
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    same_product = models.ManyToManyField('self', related_name='same_products', blank=True)
    category = models.ManyToManyField('product.Category', related_name='categories')
    who_like = models.ManyToManyField(Customer, related_name='liked_products', blank=True)
    marka = models.ManyToManyField(Marka, related_name='marka', blank=True)


    # informations
    title = models.CharField('Başlıq', max_length=100, db_index=True)
    color_title = models.CharField('Rəng adı', max_length=50, blank=True, null=True)
    color_code = ColorField('Rəng kodu', default='', blank=True, null=True)
    internal_storage = models.IntegerField('Daxili yaddaş (GB)', default=None, blank=True, null=True)
    ram = models.IntegerField('Operativ yaddaş (GB)', default=None, blank=True, null=True)
    operator_code = models.CharField('Operator code', max_length=3, default=None, blank=True, null=True)
    slug = models.SlugField('Slug', editable=False, max_length=110, unique = True, blank=True)
    sku = models.CharField('SKU', max_length=50, db_index=True)
    description = models.TextField('Ətraflı', null=True, blank=True)
    sale_count = models.IntegerField('Satış sayı', default=0)
    is_published = models.BooleanField("Paylaş", default=True)
    is_new = models.BooleanField('Yeni', default=True)
    is_new_expired = models.DateTimeField('Bitmə vaxtı', default=one_month_from_today, blank=True, null=True)
    is_featured = models.BooleanField('is_featured', default=False)
    is_discount = models.BooleanField('Endirim', default=False)

    # price info
    CHOICES = (
        (1, 'Yox'),
        (2, 'Faiz'),
        (3, 'Vahid'),
    )
    price = models.DecimalField('Qiymət', max_digits=7, decimal_places=2)
    old_price = models.DecimalField('Köhnə qiymət Price', max_digits=7, decimal_places=2, null=True, blank=True)
    discount_type = models.PositiveIntegerField("Endirim növü", choices=CHOICES, default=1)
    discount_value = models.IntegerField('Endirim dəyəri', null=True, blank=True)

    # moderations
    status = models.BooleanField('Aktiv', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('title', 'slug')
        # slug unique
        db_table = 'product'
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'
        ordering = ('-created_at', 'title')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def save(self, *args, **kwargs):        
        from .tasks import changed_is_new
        super(Product, self).save(*args, **kwargs)
        ram = self.ram if self.ram != None  else ''
        internal_storage = self.internal_storage if self.internal_storage != None  else ''
        color_title = self.color_title if self.color_title != None  else ''
        
        if self.slug:
            self.slug=''

        slug = f' {self.title} {ram} {internal_storage} {color_title}'
        self.slug = f'{slugify(slug)}'

        if self.operator_code:
            slug = f'{self.operator_code} {self.title}'
            self.slug = f'{slugify(slug)}'
        
        if self.is_new: 
            changed_is_new.apply_async(args=[self.id], eta=self.is_new_expired)

        return super(Product, self).save(*args, **kwargs)

    @property
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
    
    @property
    def get_discount(self):
        return self.price - self.get_price
    
    def get_is_new(self):
        delta = datetime.now().date() - self.created_at
        if delta.days <= 30:
            is_new = True

    def __str__(self):
        if self.operator_code not in (None, ''):
            return f'({self.operator_code}) {self.title}'
        if self.title and self.internal_storage and self.ram and self.color_title:
            return f' {self.title} {self.ram} {self.internal_storage} {self.color_title}'
        
        if self.title and self.internal_storage and self.color_title:
            return f' {self.title} {self.internal_storage} {self.color_title}'
        
        if self.title and self.ram and self.color_title:
            return f' {self.title} {self.ram} {self.color_title}'

        if self.title and self.color_title :
            return f'{self.title} {self.color_title}'

        return f'{self.title}'

class Product_details(models.Model):

    # relations
    product = models.ForeignKey('product.Product', related_name='products', default="Not", on_delete=models.CASCADE, blank=True, null=True)
    product_details_property_name = models.ForeignKey("Product_details_property_name", on_delete=models.CASCADE, related_name='product_details_property_name')
    # product_details_propert_value = models.ForeignKey("Product_details_property_value", on_delete=models.CASCADE, related_name='product_details_property_value')
    content = models.CharField('Value', max_length=50, blank=True, null=True)
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
        db_table = 'product_details'
        verbose_name = 'Məhsul detalı'
        verbose_name_plural = 'Məhsul detalları'


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
        db_table = 'detail_name'
        verbose_name = 'Detalın növü'
        verbose_name_plural = 'Detalın növləri'


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
        verbose_name = 'Şəkil'
        verbose_name_plural = 'Şəkillər'
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
        db_table = 'product_colors'
        verbose_name = 'Məhsul rəngi'
        verbose_name_plural = 'Məhsul rəngləri'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'


