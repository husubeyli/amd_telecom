from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Subscriber, Banner
# Register your models here.


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_main", 'is_second_yuxari', 'is_second_ashagi', 'is_third_sol', "is_third_sag", 'is_third_orta', 'link', 'status', 'get_image')
    list_display_links = ("title",)
    # list_filter = ("price", "category", 'is_new', 'internal_storage', 'ram', 'color_title')
    # search_fields = ('title', "category__title", "Marka")
    # readonly_fields = ('slug',)
    # inlines = [ImageInline, ProductDetailNameAdmin]
    save_on_top = True


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')


    get_image.short_description = "Image"

admin.site.register([Subscriber,])