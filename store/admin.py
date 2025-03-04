from django.contrib import admin
from .models import *

from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToFit
from imagekit.cachefiles import ImageCacheFile


admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Address)

# Register your models here.
@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = HomePage.objects.all().count()
        if count == 0:
            return True

        return False
    



@admin.register(WebSiteInfo)
class WebSiteInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = WebSiteInfo.objects.all().count()
        if count == 0:
            return True

        return False


class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFit(100)]
    format = 'JPEG'
    options = {'quality': 60 }

def cached_admin_thumb(instance):
    # `image` is the name of the image field on the model
    cached = ImageCacheFile(AdminThumbnailSpec(instance.image))
    # only generates the first time, subsequent calls use cache
    cached.generate()
    return cached

class ProductInline(admin.TabularInline):
    model = Product.size.through
    extra = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)

    list_display = ['name', 'image_display']
    image_display = AdminThumbnail(image_field=cached_admin_thumb)
    image_display.short_description = 'Image'

    readonly_fields = ['image_display']  # this is for the change form


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product',)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    readonly_fields=('OrderId', 'Address')

