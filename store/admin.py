from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = HomePage.objects.all().count()
        if count == 0:
            return True

        return False
    
admin.site.register(Category)
admin.site.register(Product)

@admin.register(WebSiteInfo)
class WebSiteInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = WebSiteInfo.objects.all().count()
        if count == 0:
            return True

        return False