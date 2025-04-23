from django.contrib import admin
from .models import manfacturer, Product, hardware
# Register your models here.
admin.site.register(manfacturer)
admin.site.register(Product)
admin.site.register(hardware)