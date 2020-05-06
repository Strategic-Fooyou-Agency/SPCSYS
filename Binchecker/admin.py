from django.contrib import admin
from Binchecker import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
                    'bin_name',
                    'exproduct_name',
                    'spec_name',
                    'process_code',
                    )


admin.site.register(models.Product, ProductAdmin)