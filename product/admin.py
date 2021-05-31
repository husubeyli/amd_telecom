from django.contrib import admin
from django.utils.safestring import mark_safe
from .common import slugify
from django.forms import SelectMultiple
# Register your models here.
from .models import (
    Product, 
    Marka, 
    Category, 
    Product_details, 
    Product_colors, 
    Product_images,
    Tag,
    Product_details_property_name,
    # Product_details_property_value,
)

admin.site.register(Product_colors)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "description", "is_main", "status", 'id')
    list_display_links = ("title",)
    readonly_fields = ('slug',)
    list_filter = ("title", "status")
    search_fields = ('title',)
    # prepopulated_fields = {'slug': ('title',)}


    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        category = form.instance
        if not category.parent.all().last():
            category.slug = slugify(f'{category.title}')
        else:
            category.slug = slugify(f'{category.parent.all().last()} {category.title}')
        category.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['parent'].widget.attrs['style'] = 'height: 160px;'
        return form


@admin.register(Marka)
class MarkaAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ("id", "title", "description", "slug")
    list_display_links = ("title",)

@admin.register(Product_images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image", "product")


class ImageInline(admin.TabularInline):
    model = Product_images
    extra = 0


@admin.register(Product_details_property_name)
class PropertyNameAdmin(admin.ModelAdmin):
    list_display = ("title", "status")


# @admin.register(Product_details_property_value)
# class PropertyValueAdmin(admin.ModelAdmin):
#     list_display = ("content", "file", "status")

admin.site.register(Product_details)
class ProductDetailNameAdmin(admin.TabularInline):
    model = Product_details
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", 'show_markas', 'internal_storage', 'ram', "is_new", 'get_color', 'get_image') #"get_image"
    list_display_links = ("title",)
    list_filter = ("price", "category", 'is_new', 'internal_storage', 'ram', 'color_title')
    search_fields = ('title', "category__title", "Marka")
    readonly_fields = ('slug',)
    inlines = [ImageInline, ProductDetailNameAdmin]
    save_on_top = True
    save_as = True #create new product easy way
    
    fieldsets = (
        ('Relations', {
            'fields': ('category','marka', 'tags', 'same_product'),
        }),
        ('Informations', {
            'fields': (('title', 'slug'), 'sku', 'internal_storage', 'ram', ('color_title', 'color_code',), 'operator_code', 'description', 'sale_count', ('is_featured',), 'status')
        }),
        ('Publishe', {
            'fields': ('is_published',)
        }),
        ('Price & Kampaniya', {
            'fields': ('price', 'is_new', 'is_new_expired', 'is_discount', 'discount_type', 'discount_value')
        }),
        # ('Price Info', {
        #     'fields': ('price', 'old_price'),
        # }),
    )

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        product = form.instance

        marka = product.marka.first() if product.marka.first() != None  else ''
        ram = product.ram if product.ram != None  else ''
        internal_storage = product.internal_storage if product.internal_storage != None  else ''
        color_title = product.color_title if product.color_title != None  else ''

        

        # if product.slug:
        #     product.title=

        
        

    def show_markas(self, obj):
        return ' '.join([product.title for product in obj.marka.all()])
    
    def show_category(self, obj):
        return ' '.join([product.title for product in obj.category.all()])

    def get_color(self, obj):
        return mark_safe(f'<div style="width: 30px !important; height: 30px !important; border-radius: 50% !important; background-color: {obj.color_code} !important"></div>')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.images.get(is_main=True).imageURL} width="50" height="60"')


    show_markas.short_description = "Marka"
    show_category.short_description = "Category"

    get_color.short_description = "Color"

    get_image.short_description = "Image"

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProductAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['category'].widget.attrs['style'] = 'height: 155px;'
        form.base_fields['marka'].widget.attrs['style'] = 'height: 155px;'
        form.base_fields['same_product'].widget.attrs['style'] = 'height: 155px;'



        return form






admin.site.register(Tag)