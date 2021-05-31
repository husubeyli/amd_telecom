from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Order, OrderItem

# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(Checkout)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "transaction_id", "complete",)
    list_display_links = ("created_at",)
    list_filter = ("complete",)
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    # remove 'get_image' from below
    list_display = ("id", "product", "quantity", "created_at")
    list_display_links = ("product",)
    list_filter = ("quantity", "product__title",)
    search_fields = ('product__title',)

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.product.images.get(is_main=True).imageURL} width="50" height="60"')
    
    
    # get_image.short_description = "Image"